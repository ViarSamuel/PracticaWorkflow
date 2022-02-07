height=players_stats$V30
height=height[2:491]
height=as.numeric(height)
height=height[!is.na(height)]

h_mean=mean(height)
hist(height,main="Height of NBA players")
lines(x=c(h_mean,h_mean), y=c(0,150), col='blue', lwd=2)
legend("topleft",lwd=2,col='blue',c("Height mean"))