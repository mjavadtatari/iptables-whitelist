input_file = open(r"input_list.txt", "r+")
output_file = open(r"output_list.txt", "w+")

text=input_file.readlines()


for i in text:
    i=i.strip()
    temp_x= 'sudo iptables -I INPUT -p tcp -m multiport --dports http,https -s "{}" -j ACCEPT \n'.format(i)
    
    output_file.write(temp_x)

input_file.close()
output_file.close()