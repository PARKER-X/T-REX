import kagglehub

# Download latest version
path = kagglehub.dataset_download("disisbig/hindi-wikipedia-articles-172k")

#path = kagglehub.dataset_download("crazydiv/oldnewspapershindi")


print("Path to dataset files:", path)