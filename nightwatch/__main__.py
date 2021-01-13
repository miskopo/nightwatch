import json
import logging
from sys import stdout

from cli_arguments import init_args


def _parse_config():
    with open("config.json") as config_file:
        return json.load(config_file)


def _setup_logger():
    _logger = logging.getLogger('nightwatch')
    logging_levels = {"INFO": logging.INFO, "DEBUG": logging.DEBUG}
    try:
        if ARGS.verbosity >= 1:
            _logger.setLevel(logging_levels["DEBUG"])
    except AttributeError:
        _logger.setLevel(logging_levels[CONFIG["debug_level"]])
    finally:
        console_handler = logging.StreamHandler(stream=stdout)
        console_handler.setLevel(_logger.getEffectiveLevel())
        _logger.addHandler(console_handler)
    return _logger


CONFIG = _parse_config()
ARGS = init_args()
logger = _setup_logger()


def main():
    logger.info(f"Target PR: {CONFIG['base_url']}{ARGS.prnumber[0]}")


if __name__ == '__main__':
    main()
