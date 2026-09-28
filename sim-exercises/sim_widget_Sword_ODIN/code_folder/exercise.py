from mcstasscript.jb_interface import SimInterface
import code_folder.Sword_ODIN_generated as sword


def make():
    return sword.make(input_path="code_folder")


def show_widget():
    instr = sword.make(input_path="code_folder")
    sim_interface = SimInterface(instr)
    sim_interface.mpi = 4
    return sim_interface.show_interface()
