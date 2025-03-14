#Arithmetic Mean  
function AM = ArithmeticMean(X,~) 
AM = mean(X); 
End 
#First Difference 
function FD = FirstDifference(X,~) 
T = length(X); 
Y = 0; 
for t = 1 : T - 1 
Y = Y + abs(X(t+1) - X(t)); 
end 
FD = (1 / (T - 1)) * Y; 
End 
#Hjorth Activity 
function HA = HjorthActivity(X,~)  
sd = std(X);  
HA = sd ^ 2; 
End 
#Hjorth Complexity 
function HC = HjorthComplexity(X,~) 
% First & second derivative 
x0  = X(:); 
40 
x1  = diff([0; x0]); 
x2  = diff([0; x1]); 
#Standard deviation of first & second derivative  
sd0 = std(x0); 
sd1 = std(x1); 
sd2 = std(x2);  
#Complexity 
HC  = (sd2 / sd1) / (sd1 / sd0); 
End 
#Hjorth Mobility 
function HM = HjorthMobility(X,~) 
#First derivative 
x0  = X(:); 
x1  = diff([0; x0]);  
#Standard deviation  
sd0 = std(x0);  
sd1 = std(x1); 
HM  = sd1 / sd0; 
end 
#Kurtosis 
function KURT = Kurtosis(X,~) 
#Kurtosis  
KURT = kurtosis(X); 
End 
#Log Root Sum of Sequential Variation 
function LRSSV = LogRootSumOfSequentialVariation(X,~) 
N = length(X);  
Y = zeros(1, N-1); 
for i = 2:N 
Y(i-1) = (X(i) - X(i-1)) ^ 2; 
end 
LRSSV = log10(sqrt(sum(Y))); 
end 
#Maximum 
function X_max = Maximum(X,~) 
X_max = max(X); 
end 
#Mean Curve Length 
function MCL = MeanCurveLength(X,~) 
N = length(X);  
Y = 0; 
for m = 2:N 
Y = Y + abs(X(m) - X(m-1)); 
end 
MCL = (1 / N) * Y; 
End 
#Median 
function X_med = Median(X,~) 
X_med = median(X); 
42 
End 
#Minimum 
function X_min = Minimum(X,~) 
X_min = min(X); 
end 
#Normalized First Difference 
function NFD=NormalizedFirstDifference(X,~) 
T = length(X);  
Y = 0;  
for t = 1 : T - 1 
Y = Y + abs(X(t+1) - X(t)); 
end 
FD  = (1 / (T - 1)) * Y;  
NFD = FD / std(X); 
End 
#Normalized Second Difference 
function NSD = NormalizedSecondDifference(X,~) 
T = length(X);  
Y = 0; 
for t = 1 : T - 2 
Y = Y + abs(X(t+2) - X(t)); 
end 
SD  = (1 / (T - 2)) * Y;  
NSD = SD / std(X); 
end  
#Second Difference 
function SD = SecondDifference(X,~) 
T = length(X);  
Y = 0; 
for t = 1 : T - 2 
Y = Y + abs(X(t+2) - X(t)); 
end 
SD = (1 / (T - 2)) * Y; 
End 
#Skewness 
function SKEW = Skewness(X,~) 
SKEW = skewness(X); 
end 
#standard deviation 
function SD = StandardDeviation(X,~) 
N  = length(X);  
mu = mean(X);  
SD = sqrt((1 / (N - 1)) * sum((X - mu) .^ 2)); 
end 
#Variance 
function VAR = Variance(X,~) 
N   = length(X);  
mu  = mean(X); 
VAR = (1 / (N - 1)) * sum((X - mu) .^ 2); 
end