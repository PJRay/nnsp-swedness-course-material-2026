from mcstasscript.jb_interface import SimInterface
import code_folder.Radiography_Lithium_Battery_generated as battery


def make():
    return battery.make(input_path="code_folder")


def show_widget():
    instr = battery.make(input_path="code_folder")
    sim_interface = SimInterface(instr)
    sim_interface.mpi = 4
    return sim_interface.show_interface()
