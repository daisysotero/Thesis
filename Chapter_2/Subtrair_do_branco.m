%Subtrair
plot(Time,(data))
hold on
plot(Time,(branco), 'r')
plot(Time,[data - branco],'k')
subtraido =[data - branco];
xlswrite('FUV485.2.xlsx', subtraido) 