class TreeNode:
    def __init__(self, data, select=False):
        self.data = data
        self.select = select
        self.children = []

    def __str__(self):
        return f'{self.data} | {self.children}'

    def __repr__(self):
        return f'Node(name={self.data})'
