from mcstasscript.jb_interface import SimInterface
import code_folder.reflectometer_alignment_generated as reflectometer


def make():
    return reflectometer.make(input_path="code_folder")


def show_widget():
    instr = reflectometer.make(input_path="code_folder")
    sim_interface = SimInterface(instr)
    sim_interface.mpi = 4
    return sim_interface.show_interface()
