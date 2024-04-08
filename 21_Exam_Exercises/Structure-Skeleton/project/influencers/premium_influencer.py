from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.85

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * PremiumInfluencer.INITIAL_PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            return int((self.followers * self.engagement_rate) * 1.5)
        elif campaign_type == "LowBudgetCampaign":
            return int((self.followers * self.engagement_rate) * 0.8)


