# import anonymizer command
# import run command
# import construct_csv command
# import collect_stats command
from GANDLF.entrypoints.patch_miner import new_way as patch_miner_command

from GANDLF.entrypoints.preprocess import new_way as preprocess_command

# import verify_install command
from GANDLF.entrypoints.config_generator import new_way as config_generator_command

# import recover_config command
from GANDLF.entrypoints.deploy import new_way as deploy_command

from GANDLF.entrypoints.optimize_model import new_way as optimize_model_command

# import generate_metrics command
# import debug_info command
# import split_csv command

cli_subcommands = {
    # TODO: add anonymizer command
    # TODO: add run command
    # TODO: add construct-csv command
    # TODO: add collect-stats command
    "patch-miner": patch_miner_command,
    "preprocess": preprocess_command,
    # TODO: add verify-install command
    "config-generator": config_generator_command,
    # TODO: add recover-config command
    "deploy": deploy_command,
    "optimize-model": optimize_model_command,
    # TODO: add generate-metrics command
    # TODO: add debug-info command
    # TODO: add split-csv command
}
