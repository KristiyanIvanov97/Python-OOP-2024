from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    INITIAL_BUDGET: float = float(5000)

    def __init__(self, campaign_id, brand, required_engagement):
        super().__init__(campaign_id, brand, HighBudgetCampaign.INITIAL_BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * 1.20

