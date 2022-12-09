class TagCloud:
    def __init__(self) -> None:
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0)+1

    # eg: tag_cloud["Python"]
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # eg: tag_cloud["python"]=4
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # eg: len(tag_cloud)
    def __len__(self):
        return len(self.tags)
    # eg: for item in tag_cloud:
    #  print(item)

    def __iter__(self):
        return iter(self.tags)
