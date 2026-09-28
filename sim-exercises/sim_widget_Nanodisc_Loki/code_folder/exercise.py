from mcstasscript.jb_interface import SimInterface
import code_folder.Nanodisc_Loki_generated as nanodisc


def make():
    return nanodisc.make(input_path="code_folder")


def show_widget():
    instr = nanodisc.make(input_path="code_folder")
    sim_interface = SimInterface(instr)
    sim_interface.mpi = 4
    return sim_interface.show_interface()
