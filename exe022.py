from sbbst import sbbst

tree = sbbst()
nums = [131, 4, 134, 135, 10, 1, 3, 21, 14, 142, 80, 146]
for num in nums:
    tree.insert(num)

print('Número de elementos:', tree.getSize())
print('Altura:', tree.getHeightTree())
print('Min valor:', tree.getMinVal())
print('Max valor:', tree.getMaxVal())
print('3ª menor valor:', tree.kthsmallest(3))
print('2ª maior valor:', tree.kthlargest(2))
print('Pré-Ordem:', tree.preOrder())
print('In-Ordem:', tree.inOrder())
print('Pós-Ordem:', tree.postOrder())
tree.delete(3)
tree.delete(128)
tree.insert(55)