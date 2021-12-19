# setwd("C:\\Users\\rober\\OneDrive\\Documents\\test_ggmap\\")
# source("test.R")

library(ggmap)


#exemple USA

# us <- c(left = -125, bottom = 25.75, right = -67, top = 49)
# map <- get_stamenmap(us, zoom = 5, maptype = "toner-lite")
#
# # print(ggmap(map))
#
# ggsave("name.png",ggmap(map))


# exemple Europe

# europe <- c(left = -12, bottom = 35, right = 30, top = 63)
# map_ue <- get_stamenmap(europe, zoom = 5,"toner-lite")
#
# print(ggmap(map_ue))

#France
#
fr <- c(left = -6, bottom = 41, right = 10, top = 52)
map_fr <- get_stamenmap(fr, zoom = 5,"toner-lite")

# print(ggmap(map_fr))


data_all <- read.csv("C:\\Users\\rober\\OneDrive\\Documents\\test_ggmap\\all_data_temperatures.csv")

#temperature moyenne

p <- ggmap(map_fr)
p <- p + geom_point(data=data_all, aes(x=lon, y=lat,color=temp), size=2)
p <- p + scale_color_gradient2(midpoint=mean(data_all$temp),  low="blue", mid="white", high="red",space = "Lab")


print(p)

ggsave("map.png")


# # temperature minimum
# p <- ggmap(map_fr)
# p <- p + geom_point(data=data_all, aes(x=lon, y=lat,color=temp_min), size=2)
# #p <- p + scale_color_gradient2(midpoint=mean(data_all$temp_min),  low="blue", mid="white", high="red",space = "Lab")
#
#
# print(p)
#
# ggsave("map_min.png")
#
# # temperature maximum
#
#
# p <- ggmap(map_fr)
# p <- p + geom_point(data=data_all, aes(x=lon, y=lat,color=temp_max), size=2)
# p <- p + scale_color_gradient2(midpoint=mean(data_all$temp_max),  low="blue", mid="white", high="red",space = "Lab")
#
#
# print(p)
#
# ggsave("map_max.png")








