from GANDLF.cli import copyrightMessage


# import anonymizer command
# import run command
# import construct_csv command
# import collect_stats command
# import patch_miner command
# import preprocess command
# import verify_install command
# import config_generator command
# import recover_config command
# import deploy command
# import optimize_model command
# import generate_metrics command
from GANDLF.entrypoints.debug_info import new_way as debug_info_command
# import split_csv command


def append_copyright_to_help(command_func):
    command_func.__doc__ = (
        copyrightMessage
        if command_func.__doc__ is None
        else (command_func.__doc__ + "\n\n" + copyrightMessage)
    )
    return command_func


cli_subcommands = {
    # TODO: add anonymizer command
    # TODO: add run command
    # TODO: add construct-csv command
    # TODO: add collect-stats command
    # TODO: add path-miner command
    # TODO: add preprocess command
    # TODO: add verify-install command
    # TODO: add config-generator command
    # TODO: add recover-config command
    # TODO: add deploy command
    # TODO: add optimize-model command
    # TODO: add generate-metrics command
    "debug-info": debug_info_command,
    # TODO: add split-csv command
}
