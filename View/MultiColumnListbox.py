'''
Here the TreeView widget is configured as a multi-column listbox
with adjustable column width and column-header-click sorting.
'''
try:
    import Tkinter as tk
    import tkFont
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk

class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""
    tree = None
    roomHeader = None
    roomList = None
    container = None

    def __init__(self, container):
        self.tree = None
        self.container = container
        self.roomHeader = ['Idx', 'seller', 'item name']
        self.roomList = [('1', '1', '1')]
        self.roomList[0]
        self._setup_widgets()
        self.addRoom(self.roomList)

    def _setup_widgets(self):
        self.container.place(relx=0.05, rely=0.18, relheight=0.6, relwidth=0.9)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(self.container, columns=self.roomHeader, show="headings")
        self.tree.lift()
        vsb = ttk.Scrollbar(self.container, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self.container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=self.container)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.container)
        hsb.grid(column=0, row=1, sticky='ew', in_=self.container)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        for col in self.roomHeader:
            self.tree.heading(col, text=col.title(), command=lambda c=col: self.sortby(c, 0))
            # adjust the column's width to the header string
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

    # Add room to the ListBox
    def addRoom(self, roomList):
        self.roomList = roomList
        self.tree.delete(*self.tree.get_children())
        for item in self.roomList:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(self.roomHeader[ix], width=None) < col_w:
                    self.tree.column(self.roomHeader[ix], width=col_w)

    # Sort the data in the List
    def sortby(self, col, descending):
        """sort tree contents when a column header is clicked on"""
        # grab values to sort
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]
        # if the data to be sorted is numeric change to float
        # now sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            self.tree.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
            self.tree.heading(col, command=lambda col=col: self.sortby(col, int(not descending)))