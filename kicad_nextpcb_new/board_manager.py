from pcbnew import GetBoard , LoadBoard
import wx
import os

class BoardManager : 
    def __init__(self , board) -> None:
        if board  is None:
             raise("Empty kicad pcb board!")
        self._board = board

    @property
    def board(self):
        return self._board
        
def load_board_manager():
    for fp in   "D://KiCad/7.0/share/kicad/demos/complex_hierarchy/complex_hierarchy.kicad_pcb",'D:\\KiCad\\7.0\\share\\kicad\\demos\\complex_hierarchy\\complex_hierarchy.kicad_pcb':
        if os.path.exists(fp):
            return LoadBoard(fp)
            # return BoardManager(LoadBoard(fp))
    #Setup board
    board = GetBoard()
    if board:
        return board
        # return BoardManager(board)
    else:
        dlg = wx.FileDialog(
            None, message="Choose a kicad pcb file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="*.kicad_pcb",
            style=wx.FD_OPEN | wx.FD_MULTIPLE |
                wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                wx.FD_PREVIEW
            )

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()
            if len(paths):
                    board = LoadBoard(paths[0])
        dlg.Destroy()            
        return board
        return BoardManager(board)