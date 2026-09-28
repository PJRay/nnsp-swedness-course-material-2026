from mcstasscript.jb_interface import SimInterface
import code_folder.Ni_TAS_generated as ni_tas


def make():
    return ni_tas.make(input_path="code_folder")


def show_widget():
    instr = ni_tas.make(input_path="code_folder")
    sim_interface = SimInterface(instr)
    sim_interface.mpi = 4
    return sim_interface.show_interface()
