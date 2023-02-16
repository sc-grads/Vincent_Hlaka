# Ex 40

my_str = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'

# YOUR CODE STARTS HERE


my_list = my_str.split()
# my_list is ['wlo1', 'Link', 'encap:Ethernet', 'HWaddr', 'b4:6d:83:77:85:f3']


# We concatenate the first list element, '!' and the last list element
interface_mac = my_list[0] + '!' + my_list[-1]
print(interface_mac)  # => wlo1!b4:6d:83:77:85:f3
