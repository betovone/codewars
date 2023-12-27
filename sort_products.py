
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
    print(dic_ordenado)
    
    sorted_sections = dict(sorted(dic_sections.items(), key=lambda item: item[1]))
    
    for p in all_products:
        if not p.item_from_template and p.section_id:
            if p.section_id not in dic_sections.keys():
                raise Exception("La seccion del producto no está en el presupuesto")
            
            id_seq_nuevo_prod = buscar_seq_prox_section(p.section_id, sorted_sections)  
            for k, v in dic_ordenado.items():
                if v >= id_seq_nuevo_prod:
                    dic_ordenado[k] = v + 1
                    if k in dic_sections.keys():
                        dic_sections[k] = v + 1 
                        sorted_sections = dict(sorted(dic_sections.items(), key=lambda item: item[1]))
            dic_ordenado[p.id] = id_seq_nuevo_prod
        else:
            dic_ordenado[p.id] = p.sequence
    
    
    
    d = dict(sorted(dic_ordenado.items(), key=lambda x: x[1]))
    
    print(d)
            
    
    return d
    

