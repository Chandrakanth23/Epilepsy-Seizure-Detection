tic; 
clc; 
clear all; 
close all; 
clearvars; 
load('Data_n.mat'); 
load('Label_n.mat'); 
load('tdata_n.mat'); 
load('tLabel_n.mat'); 
data=Data; 
label=Label; 
t_data=tData; 
t_label=tlabel; 
t = templateTree('MaxNumSplits',6);  
rusTree=fitcensemble(data,label,'Method','AdaBoostM2','NumLearningCycles',50,'Learners',t,'LearnRate',1); 
figure; 
plot(loss(rusTree,data,label,'mode','cumulative')); 
grid on; 
xlabel('Number of trees'); 
ylabel('Test classification error'); 
title('No of Trees VS Classification error'); 
Yfit = predict(rusTree,t_data); 
accuracy = mean(t_label==Yfit); 
[confMat,order] = confusionmat(t_label,Yfit); 
figure; 
cm= confusionchart(t_label,Yfit,'Title','Confusion Chart'); 

sortClasses(cm,{'1','2','3'}) 
confMat1 = bsxfun(@rdivide,confMat,sum(confMat,2))*100; 
confMat2 = bsxfun(@rdivide,confMat,sum(confMat))*100; 
Precision=[confMat1(1,1);confMat1(2,2);confMat1(3,3)]; 
Recall=[confMat2(1,1);confMat2(2,2);confMat2(3,3)]; 
s_r=sum(confMat); 
s_c=sum(confMat,2); 
fp_1=(s_c(1)-confMat(1,1)); 
fp_2=(s_c(2)-confMat(2,2)); 
fp_3=(s_c(3)-confMat(3,3)); 
fn_1=(s_r(1)-confMat(1,1)); 
fn_2=(s_r(2)-confMat(2,2)); 
fn_3=(s_r(3)-confMat(3,3)); 
ts=sum(s_r,2); 
acc1=(trace(confMat)/ts)*100; 
%%Specificity 
TN_1=ts-s_r(1)-s_c(1)+confMat(1,1); 
TN_2=ts-s_r(2)-s_c(2)+confMat(2,2); 
TN_3=ts-s_r(3)-s_c(3)+confMat(3,3); 
s1=(TN_1/(TN_1+fp_1))*100; 
s2=(TN_2/(TN_2+fp_2))*100; 
s3=(TN_3/(TN_3+fp_3))*100; 
Sp=[s1;s2;s3]; 
a1=(2*confMat1(1,1)*confMat2(1,1))/(confMat1(1,1)+confMat2(1,1)); 

a2=(2*confMat1(2,2)*confMat2(2,2))/(confMat1(2,2)+confMat2(2,2)); 
a3=(2*confMat1(3,3)*confMat2(3,3))/(confMat1(3,3)+confMat2(3,3)); 
F_Score=[a1;a2;a3]; 
Normal=confMat(:,1);Pre_Seizure=confMat(:,2);Seizure=confMat(:,3); 
name={'Normal','Pre_Seizure','Seizure'}; 
Confusionmatrix=table(Normal,Pre_Seizure,Seizure,'Rownames',name) 
overall_acc=acc1 
Performancetable=table(Precision,Recall,Sp,F_Score,... 'Rownames',name) 