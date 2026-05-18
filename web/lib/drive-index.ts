/** Static map: MCP deal_id → Drive folder URL.
 *
 * Sourced by listing the Atlas Crossing Partners Drive root and matching
 * folder names against MCP deal codenames. Update when deals are added or
 * folders moved. Document-level linking is not wired yet — clicks land in
 * the deal's top-level Drive folder; the user navigates from there.
 */

const DEAL_FOLDER: Record<string, string> = {
  // Active diligence
  deal_project_aurora_2026:    "1H88djEKMk6l_BJSob7eJ28h9PyZpfkye",
  deal_project_brookline_2026: "1B5Cn-C5GtfmvUwr9lNyKt_ZfROddLMlL",
  deal_project_cascade_2025:   "1v6kwji-sO6usqcjG16Kt0BYw3A1No-JZ",
  deal_project_driftwood_2026: "1BiV5haQqFK6l26o3BsfgXMLse-_1FQqy",
  deal_project_everest_2026:   "1FUdJGiFo4TfV4_VrLZf8Qur0-QBVyPtY",

  // Closed-exited
  deal_halcyon_pet_foods_2017:               "1eso6GlFtbCk0Mrjf8NbOtyJrkrAWM56M",
  deal_cardinal_filtration_co_2014:          "1LihI5TPBpe1rgvG3y2N5GlfFxx-6JtIh",
  deal_meridian_safety_systems_2012:         "1AQjatG7WieLDqOXCidDpeStD7RlsI_Yv",
  deal_precision_asset_inspections_inc_2016: "1z9Eqdm-vfvxTJTWe4Pf4FAoSFqUo8JwE",

  // Closed-held (portfolio)
  deal_vanguard_auto_2021:               "13LHyxbSumDr5Y7OWRk0ELTaf-fZRYFqh",
  deal_pinecrest_foods_2022:             "13xgRJZfFwZZ6mZ4fltI7SswlL9H141Pr",
  deal_wholesum_foods_distribution_2022: "1uN6K-xJbDotYiHZg1weCi6KXOwTVpAk0",
  deal_crestview_coffee_2019:            "1NUiKRiSbpoO1s1cOXMVJ1XkNXRD1Sgba",

  // Dead
  deal_project_pegasus_2021:  "1eh9TrM12wUJdeOyH33ASOMn-uyiE9HeN",
  deal_project_quarry_2019:   "1ZJDC2AlXiavew4YJ9766hFYATHza3toA",
  deal_project_sundial_2022:  "1oSqBFun4YmZ8BaEYXQwpFjg5uTLNZ1DU",
  deal_project_tideway_2023:  "1RM9FqZ39rxyPWME7LtKXr7dfgNP0AzHu",
  deal_project_vellum_2024:   "1T3Zy1abkMsqswsrlIHvNoZ4-9ylEN8-d",
  deal_project_beacon_2023:   "132dbrCtyPSi6INj0rovRCvtDSwK7K4tC",
  deal_project_ember_2024:    "1M6diVI_x10F9qQGfGJvowOCSBcREu_3i",
};

export function driveUrlForDeal(dealId: string | undefined | null): string | undefined {
  if (!dealId) return undefined;
  const folder = DEAL_FOLDER[dealId];
  return folder ? `https://drive.google.com/drive/folders/${folder}` : undefined;
}
