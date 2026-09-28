from mcstasscript.jb_interface import SimInterface
import code_folder.ESS_HEIMDAL_generated as heimdal


def make():
    return heimdal.make(input_path="code_folder")


def show_widget():
    instr = heimdal.make(input_path="code_folder")
    sim_interface = SimInterface(instr)
    sim_interface.mpi = 4
    return sim_interface.show_interface()
