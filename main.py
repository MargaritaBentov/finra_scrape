import links


def main():
    driver = links.initialize_driver()
    links.scrape_links(driver,
                       "https://www.finra.org/finra-data/browse-catalog/"
                       "short-sale-volume-data/daily-short-sale-volume-files")
    driver.quit()


if __name__ == "__main__":
    main()
