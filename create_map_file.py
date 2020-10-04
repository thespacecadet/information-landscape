# process data and create txt file that writes a map in it that fits vosviewer's required structure

def create_map(filename,som_map,subject_lists,weights):
    f= open(filename+".txt","w+")

    vos_viewer_map_data = []
    for line in range(len(som_map)):
        for index_in_line in range(len(som_map)):
            if som_map[line][index_in_line] != (-1):
                index_of_subject = som_map[line][index_in_line]
                subject_name = subject_lists[index_of_subject][0]
                y_value = str(line)
                x_value = str(index_in_line)
                weight = str(weights[subject_name])
                vos_viewer_map_data.append([subject_name,x_value,y_value,weight])
                e = 2
    f.write("id\tlabel\tx\ty\tweight<Amount of Abstracts>\n")
    for i in range(len(vos_viewer_map_data)):
        f.write(str(i)+"\t"+vos_viewer_map_data[i][0]+"\t"+vos_viewer_map_data[i][1]+"\t"+vos_viewer_map_data[i][2]+"\t"+vos_viewer_map_data[i][3]+"\n")

    return f