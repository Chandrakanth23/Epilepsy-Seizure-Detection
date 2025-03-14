clear all; 
close all; 
CLC; 
X = load('S001.txt'); 
Y = load('N001.txt'); 
Z = load('Z001.txt'); 
Fs = 173.61; 
t = 0:1/Fs:(4097*1/Fs)-1/Fs; 
% Plot sample signal 
subplot(3,1,1); 
plot(t,X);  grid on 
xlabel('Number of samples'); 
ylabel('Amplitude'); 
subplot(3,1,2); 
plot(t,Y);  grid on 
xlabel('Number of samples'); 
ylabel('Amplitude'); 
subplot(3,1,3); 
plot(t,Z);  grid on 
xlabel('Number of samples'); 
ylabel('Amplitude'); 

%% extracting required features (without parameter )  
X = load('S003.txt'); 
Fs = 173.61; 
t = 0:1/Fs:(4097*1/Fs)-1/Fs; 
opts.alpha = 2; 
opts.fs = 500; 
 
 f1 = feeg('mcl', X)  
 % f2 = feeg('ha', X) %std devistn expo values 
 f3 = feeg('hm', X)  
 f4 = feeg('hc', X)  
 f5 = feeg('1d', X)  
 f6 = feeg('n1d', X)  
 f7 = feeg('2d', X)  
 f8 = feeg('n2d', X) 
 % f9 = feeg('me', X) 
 f10 = feeg('mte', X) 
 f11 = feeg('lrssv', X)  
 f12 = feeg('te', X)  
 % f13 = feeg('sh', X)  %NaN  
 % f14 = feeg('le', X) %Inf 
 f15 = feeg('re', X); 
 f16 = feeg('am', X);  
 f17 = feeg('sd', X) ; 
 % f18 = feeg('var', X) %same as Ha i.e std deviatn 
 f19 = feeg('md', X); 
 f20 = feeg('max', X); 
 f21 = feeg('min', X) ; 
 opts.order = 4; 
 % f22 = feeg('ar', X) %AR model parameter can be considered 
 f23 = feeg('kurt', X);  
 f24 = feeg('skew', X); 
 f25 = feeg('bpd', X,opts); 
 f26 = feeg('bpt', X,opts) ; 
 f27 = feeg('bpa', X,opts) ; 
 f28 = feeg('bpb', X,opts); 
f29 = feeg('bpg', X,opts); 
f30 = feeg('rba', X,opts); 
% Feature vector 
feat 
[f1,f3,f4,f5,f6,f7,f8,f10,f11,f12,f15,f16,f17,f19,f20,f21,f23,f24,f25,f26,f27,f28,f29,f30]; 
Data = normalize(feat) 
save Data.mat Data 
% whos("-file","Data.mat") 
% Data = normalize(feat) 
% save("Data.mat","Nr","-append")