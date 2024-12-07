clear;
clf;

nbins = 8;  % adjust as needed
scores = [852, 834, 817, 789, 753, 744, 695, 690, 680, 661, 638, 601, 581, 579, 568, 536, 533, 523, 506, 505, 497, 184, 142, 136, 119, 113, 109, 108, 101, 98, 78, 77, 70, 66, 58, 56, 0];
% % scores = scores(scores > 0);
% scores = scores(scores > 400);
h = histogram(scores, nbins, 'Normalization', 'pdf');

hold on
% x = linspace(min(scores), 900, 100);
% k = 2;  % try different values between 1-4
% xm = min(scores);
% k = 1/mean(log(scores/min(scores))); % MLE estimator for k
% pareto = (k*xm^k)./(x.^(k+1));
% % pareto = pareto * 10;
% pareto = pareto * max(h.Values)/max(pareto);
% plot(x, pareto, 'r-', 'LineWidth', 2)

% probplot('pareto', scores)
pd = fitdist(scores', 'GeneralizedPareto');
k = pd.k;  % shape parameter
sigma = pd.sigma;  % scale parameter
theta = pd.theta;  % threshold parameter
x = linspace(min(scores), max(scores), 100);
y = gppdf(x, k, sigma, theta);  % GPD probability density function
y = y * max(h.Values)/max(y);   % normalize to match histogram height

