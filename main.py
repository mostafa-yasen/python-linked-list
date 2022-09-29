
class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def __repr__(self):
    return f"<Node: data={self.data}>"

class LinkedList:
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head is None

  def append(self, node: Node) -> None:
    if not self.head:
      self.head = node
      return

    tail = self.head
    while tail.next is not None:
      tail = tail.next

    tail.next = node

  def prepend(self, node: Node) -> None:
    node.next = self.head
    self.head = node

  def print(self):
    current = self.head
    end = " => "
    while current:
      if current.next is None:
        end = "\n"
      print(current.data, end=end)
      current = current.next

    print()

  def remove(self, key: any):
    current = self.head
    previous = None

    if not current:
      raise Exception("Trying to remove from empty linked list")

    while current and current.data != key:
      previous = current
      current = current.next

    if previous is None:
      self.head = current.next

    elif current is not None:
      previous.next = current.next
      current.next = None
      del current

    else:
      raise Exception(f"Element '{key}' does not exist in the linked list")


    return self

  def get_last_node(self):
    last = self.head
    if last is None:
      return last
    
    while last.next is not None:
      last = last.next

    return last

def main(*args, **kwargs):
  linked_list = LinkedList()
  first_node = Node("First")
  second_node = Node("Second")
  third_node = Node("Third")

  linked_list.append(first_node)
  linked_list.prepend(second_node)
  linked_list.prepend(third_node)

  linked_list.print()

  linked_list.remove(second_node.data)
  linked_list.print()

if __name__ == "__main__":
  main()
