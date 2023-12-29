
prox_seq_sin_section = 1000

def buscar_seq_prox_section(id_section, sorted_sections):
    for k, v in sorted_sections.items():
        if k != id_section:
            return v
    prox_seq_sin_section += 1
    return prox_seq_sin_section

def sort_products(all_sections, all_products):
    dic_ordenado = {}
    dic_sections = {s.id: s.sequence for s in all_sections}
    dic_products = {p.id: p.sequence for p in all_products if p.item_from_template}
    dic_ordenado.update(dic_sections)
    dic_ordenado.update(dic_products)
    # print(dic_ordenado)
    
    sorted_sections = dict(sorted(dic_sections.items(), key=lambda item: item[1]))
    
    for p in all_products:
            if p.section_id:
                if p.section_id not in dic_sections.keys():
                    raise Exception("La seccion del producto no está en el presupuesto")
            
            if not p.item_from_template and p.section_id:
                id_seq_nuevo_prod = buscar_seq_prox_section(p.section_id, sorted_sections)  
            else:
                continue
            
            for k, v in dic_ordenado.items():
                if v >= id_seq_nuevo_prod:
                    dic_ordenado[k] = v + 1
                    if k in dic_sections.keys():
                        dic_sections[k] = v + 1 
                        sorted_sections = dict(sorted(dic_sections.items(), key=lambda item: item[1]))
            dic_ordenado[p.id] = id_seq_nuevo_prod
        # else:
        #    dic_ordenado[p.id] = p.sequence
    
    
    
    
    
    d = dict(sorted(dic_ordenado.items(), key=lambda x: x[1]))
    
    # print(d)
            
    
    return d
    

def ordering_products_in_sections(all_sections, all_products, all_template_products):
        ultima_sequence = 1
        ultima_sequence_sin_seccion = 1000
        dic_ordenado_de_lineas = {}
        sections = {}
        section_anterior = ""
        for line_template in all_template_products:
            dic_ordenado_de_lineas[line_template.id] = ultima_sequence
            if line_template.display_type == "line_section":
                section_anterior = line_template.name.lower()
                sections[line_template.name.lower()] = {"inicio": ultima_sequence, "fin": ultima_sequence}
            else:
                if section_anterior and section_anterior in sections:  # and not line_template.product_id.section_id:
                    sections[section_anterior]["fin"] = ultima_sequence
            ultima_sequence += 1

        for line_section in all_sections:
            if line_section.name.lower() not in sections:
                sections[line_section.name.lower()] = {"inicio": ultima_sequence, "fin": ultima_sequence}
                dic_ordenado_de_lineas[line_section.id] = ultima_sequence
                ultima_sequence += 1
            
        for line_product in all_products:
            if line_product.product_id.section_id:
                if (
                    line_product.product_id.section_id.name.lower()
                    not in all_sections.mapped(lambda x: x.name.lower())
                ):
                    msg = _(
                        "The product XXX cannot be added because it does not match any Budget section, please check the configuration of the product"
                    )
                    msg = msg.replace("XXX", line_product.product_id.name)
                    raise exceptions.ValidationError(msg)
                elif line_product.product_id.section_id.name.lower() in sections:
                    nuevo_fin_section = sections[line_product.product_id.section_id.name.lower()]["fin"] + 1
                    prod_sequence = nuevo_fin_section
                    for linea, seq in dic_ordenado_de_lineas.items():
                        if seq >= prod_sequence:
                            dic_ordenado_de_lineas[linea] = seq + 1
                    dic_ordenado_de_lineas[line_product.id] = prod_sequence
                    # ultima_sequence += 1
                    for nombre_sec, datos_sec in sections:
                        if datos_sec["inicio"] >= prod_sequence:
                            sections[nombre_sec]["inicio"] += 1
                            sections[nombre_sec]["fin"] += 1
                        elif datos_sec["inicio"] < prod_sequence <= datos_sec["fin"]:
                            sections[nombre_sec]["fin"] += 1
                    sections[line_product.product_id.section_id.name.lower()]["fin"] = nuevo_fin_section
            else:
                dic_ordenado_de_lineas[line_product.id] = ultima_sequence_sin_seccion
                ultima_sequence_sin_seccion += 1
        return dic_ordenado_de_lineas
    
    
def _ordering_by_sections(self, order_id):
        all_sections = self.search(
            [("product_id", "=", None), ("order_id", "=", order_id)], order="id"
        )
        all_products = self.search(
            [("product_id", "!=", None), ("item_from_template", "=", False), ("order_id", "=", order_id)], order="id"
        )
        all_template_products = self.search(
            [("item_from_template", "=", True), ("order_id", "=", order_id)], order="id"
        )
        dic_ordenado_de_lineas = self.ordering_products_in_sections(
            all_sections, all_products, all_template_products
        )
        for key, value in dic_ordenado_de_lineas.items():
            self.browse(key).write({"sequence": value})
        return

