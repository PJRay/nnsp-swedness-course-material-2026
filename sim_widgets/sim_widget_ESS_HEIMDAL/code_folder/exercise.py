from mcstasscript.jb_interface import SimInterface
import code_folder.ESS_HEIMDAL_generated as heimdal


def make():
    return heimdal.make(input_path="code_folder")


def make_widget_interface():
    sim_interface = SimInterface(make())
    sim_interface.mpi = 4
    return sim_interface


def show_widget():
    return make_widget_interface().show_interface()
