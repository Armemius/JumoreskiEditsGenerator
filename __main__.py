import spdlog as spd

logger = spd.ConsoleLogger("jumoreski_generator")
logger.set_level(spd.LogLevel.DEBUG)


def main():
    logger.info("Starting utility")

    # TODO

    logger.info("Job done!")


if __name__ == "__main__":
    main()
