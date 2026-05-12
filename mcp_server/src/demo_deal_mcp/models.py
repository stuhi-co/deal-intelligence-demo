"""Shared Pydantic models and enums for tool inputs/outputs.

Kept lightweight: most tools return dict[str, Any] for flexibility, but tools that
take structured CompanyProfile inputs use these models so Claude Desktop sees a clean schema.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field


class Sector(StrEnum):
    healthcare_services = "healthcare_services"
    industrial_distribution = "industrial_distribution"
    tech_enabled_services = "tech_enabled_services"
    business_services = "business_services"
    consumer_products = "consumer_products"
    manufacturing = "manufacturing"
    specialty_chemicals = "specialty_chemicals"


class DealStatus(StrEnum):
    active_diligence = "active_diligence"
    closed_exited = "closed_exited"
    closed_held = "closed_held"
    passed = "passed"
    dead = "dead"


class DealType(StrEnum):
    platform = "platform"
    add_on = "add_on"
    carve_out = "carve_out"
    take_private = "take_private"
    minority = "minority"


class Geography(StrEnum):
    northeast_us = "northeast_us"
    southeast_us = "southeast_us"
    midwest_us = "midwest_us"
    west_us = "west_us"
    national = "national"


class DocType(StrEnum):
    cim = "cim"
    teaser = "teaser"
    management_presentation = "management_presentation"
    process_letter = "process_letter"
    loi = "loi"
    expert_call = "expert_call"
    ic_memo = "ic_memo"
    dd_report = "dd_report"
    financial_model = "financial_model"
    board_package = "board_package"
    quarterly_financials = "quarterly_financials"
    returns_summary = "returns_summary"
    qofe = "qofe"
    vdd_model = "vdd_model"
    funds_flow = "funds_flow"
    ioi_tracker = "ioi_tracker"
    final_bid_comparison = "final_bid_comparison"


class ExitType(StrEnum):
    strategic_sale = "strategic_sale"
    secondary_buyout = "secondary_buyout"
    ipo = "ipo"
    held = "held"


class ThesisTheme(StrEnum):
    roll_up = "roll_up"
    market_consolidation = "market_consolidation"
    founder_transition = "founder_transition"
    margin_expansion = "margin_expansion"
    recurring_revenue = "recurring_revenue"
    premiumization = "premiumization"
    operational_excellence = "operational_excellence"


class RiskTheme(StrEnum):
    management_quality = "management_quality"
    payer_concentration = "payer_concentration"
    customer_concentration = "customer_concentration"
    regulatory_exposure = "regulatory_exposure"
    cyclicality = "cyclicality"
    integration_risk = "integration_risk"
    commodity_exposure = "commodity_exposure"
    private_label_pressure = "private_label_pressure"
    founder_dependency = "founder_dependency"
    supply_chain_concentration = "supply_chain_concentration"
    platform_dependency = "platform_dependency"


class CompanyProfile(BaseModel):
    """Lightweight profile of a target/portco/market company used for similarity searches."""

    name: Optional[str] = None
    sector: Optional[str] = None
    subsector: Optional[str] = None
    geography: Optional[str] = None
    revenue_usd: Optional[float] = Field(None, description="LTM revenue in USD")
    ebitda_usd: Optional[float] = Field(None, description="LTM EBITDA in USD")
    ebitda_margin: Optional[float] = None
    revenue_cagr_3yr: Optional[float] = None
    thesis_themes: list[str] = Field(default_factory=list)
    risk_flags: list[str] = Field(default_factory=list)
