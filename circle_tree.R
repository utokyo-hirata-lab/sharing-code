#circle_tree.R
library(ape)
library(Biostrings)
library(ggplot2)
library(ggtree)

data(chiroptera, package="ape")
groupInfo <- split(chiroptera$tip.label, gsub("_\\w+", "", chiroptera$tip.label))
chiroptera <- groupOTU(chiroptera, groupInfo)
pdf("circle_tree.pdf") #名前をつけたpdf用のキャンバスを用意
ggtree(chiroptera,aes(color=group),layout='circular')+geom_tiplab(size=1,aes(angle=angle))
dev.off() #描画デバイスを閉じる
