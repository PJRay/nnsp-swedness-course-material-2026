from mcstasscript.jb_interface import SimInterface
import code_folder.SANSsimple_generated as sans


def make():
    return sans.make(input_path="code_folder")


def show_widget():
    instr = sans.make(input_path="code_folder")
    sim_interface = SimInterface(instr)
    sim_interface.mpi = 4
    return sim_interface.show_interface()
