from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    INITIAL_BUDGET = float(2500)

    def __init__(self, campaign_id, brand, required_engagement):
        super().__init__(campaign_id, brand, LowBudgetCampaign.INITIAL_BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * 0.90

