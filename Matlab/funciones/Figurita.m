function [ positive,negative ] = Figurita( rho,adj_rho,effects,flavors ,elsupertitulo)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

x0=20;
y0=50;
width=1000;
height=500;

figure;
set(gcf,'units','points','position',[x0,y0,width,height])
colormap jet
subplot(1,2,1)
imagesc(rho)
caxis([-0.5,0.5])
title('Uncorrected')

xlabel('Sabores')
set(gca,'XTick',1:size(rho,2))
set(gca,'XTickLabel',flavors)
set(gca,'XTickLabelRotation',90)

ylabel('Efectos')
set(gca,'YTick',1:size(rho,1))
set(gca,'YTickLabel',effects)
% set(gca,'YTickLabelRotation',90)

colorbar

subplot(1,2,2)
imagesc(adj_rho)
caxis([-0.5,0.5])
title('FDR p<05')
ylabel('Efectos')
xlabel('Sabores')
set(gca,'XTick',1:size(rho,2))
set(gca,'XTickLabel',flavors)
set(gca,'XTickLabelRotation',90)
suptitle(elsupertitulo)

[positive,negative] = asoc_effects(adj_rho,effects,flavors);

end

