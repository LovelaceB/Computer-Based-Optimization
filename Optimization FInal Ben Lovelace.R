library(binaryLogic)
library(mcga)
library(DescTools)
library(gdata)
f <- function(x) abs(x-5) + sin(x-5) + 5
itNum <- 200
mate <- function(p1,p2,p3,p4){

  p1H1 <- p1[1:3]
  p1H2 <- p1[4:5]
  p2H1 <- p2[1:3]
  p2H2 <- p2[4:5]
  p3H1 <- p3[1:3]
  p3H2 <- p3[4:5]
  p4H1 <- p4[1:3]
  p4H2 <- p4[4:5]
  
  originalParents <- c(p1H1,p1H2,p2H1,p2H2,p3H1,p3H2,p4H1,p4H2)
  children <- c(p2H1,p1H2,p1H1,p2H2,p4H1,p3H2,p3H1,p4H2)
  
  newPop <- c(originalParents,children)
  newPopMatrix <- matrix(data = newPop, nrow = 8, ncol = 5, byrow = TRUE)
  return(newPopMatrix)
}

compareAndRank <- function(popMatrix) {
  order <- numeric(0)
  tempRow <- numeric(0)
  newEvalMatrix <- matrix(data = NA, nrow = 8, ncol = 6, byrow = TRUE)
  for (i in 1:8){
    tempBin <- popMatrix[i,]
    tempDec <- binary2decimal(tempBin)
    eval <- f(tempDec)
    order[i] <- eval 
    tempRow <- c(tempBin,eval)
    newEvalMatrix[i,] = tempRow
  }
  newEvalMatrix <- newEvalMatrix[order(newEvalMatrix[,ncol(newEvalMatrix)]),]
  rankedFitnessMatrix <- newEvalMatrix[,-6]
  return(rankedFitnessMatrix)
  order <- sort(order, decreasing = FALSE)

}

mutate <- function(rankedPopMatrix) {
  #calculating number of mutations, we're going to mutate 20% of the population
  # number of mutations = .20*7*5 = 7 
  colm <- runif(7,1,5)
  rows <- runif(7,2,8)
  colm <- ceiling(colm)
  rows <- ceiling(rows)
  replaceArray <- c(rbind(rows, colm))
  a <- rankedPopMatrix[cbind(rows, colm)]
  for (i in 1:7){
    if (a[i] == 1){
      a[i]<- 0
    }else{
      a[i] <- 1
    }
  }
  rankedPopMatrix <- replace(rankedPopMatrix, cbind(rows, colm), a)
  return(rankedPopMatrix)
}

#creating an inital population of 8
initial <- sample(c(0,1), 40, replace = TRUE)
initialPop <- matrix(data = initial, nrow = 8, ncol = 5, byrow = TRUE)


population <- initialPop

for (j in itNum){
  population <- compareAndRank(population)
  population <- mate(population[1,],population[2,],population[3,],population[4,])
  population <- mutate(population)
  population <- compareAndRank(population)
  potentialanswer <- population[1,]
  potentialanswer <- binary2decimal(potentialanswer)
  if(potentialanswer == 5){
    break
  }
}

answer <- population[1,]
answer <- binary2decimal(answer)
answer

