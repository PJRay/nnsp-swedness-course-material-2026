from mcstasscript.jb_interface import SimInterface
import code_folder.SimplePowderDiffractometer_generated as PowdDiffr

def make():
    # simple function to provide instrument if they want to play with it
    return PowdDiffr.make(input_path="code_folder")

def show_widget():
    instr = PowdDiffr.make(input_path="code_folder")
    sim_interface = SimInterface(instr)
    sim_interface.mpi = 4
    return sim_interface.show_interface()
