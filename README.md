# \# 🍽️ Restaurant Channel Profitability Analysis

# 

# \## 📌 Problem Statement

# 

# Despite having access to detailed cost and profit data, restaurant operators often lack:

# 

# \- A side-by-side comparison of channel profitability  

# \- Visibility into commission drag vs delivery cost  

# \- Understanding of which channels erode margins despite high revenue  

# \- Evidence to guide channel prioritization or renegotiation strategies  

# 

# As a result, many restaurants unintentionally scale low-margin or loss-making channels.

# 

# \---

# 

# \## 🎯 Primary Objectives

# 

# \- Compare net profitability across In-Store, Uber Eats, DoorDash, and Self-Delivery  

# \- Quantify margin erosion due to commissions and delivery costs  

# \- Identify the most cost-efficient channel per restaurant type  

# 

# \---

# 

# \## 📊 Secondary Objectives

# 

# \- Support data-driven channel prioritization  

# \- Provide financial evidence for aggregator negotiations  

# \- Highlight self-delivery ROI thresholds  

# 

# \---

# 

# \## 🗂️ Dataset Description

# 

# | Column | Description |

# |--------|-------------|

# | RestaurantID | Unique identifier for each restaurant branch |

# | RestaurantName | Name of the restaurant establishment |

# | CuisineType | Category of food served (e.g., Burgers, Pizza) |

# | Segment | Business model classification (e.g., Cafe, QSR) |

# | Subregion | Geographical area within Auckland (e.g., North Shore) |

# | GrowthFactor | Month-over-month growth multiplier (0.99–1.05) |

# | AOV | Average order value per transaction ($29.79–$47.23) |

# | MonthlyOrders | Total number of transactions across all channels per month |

# | InStoreOrdersCount | Total number of on-premises (walk-in) orders |

# | UberEatsOrdersCount | Total number of orders placed via Uber Eats |

# | DoorDashOrdersCount | Total number of orders placed via DoorDash |

# | SelfDeliveryOrdersCount | Orders delivered by restaurant-managed delivery staff |

# | InStoreRevenue | Gross revenue generated from in-store dining |

# | UberEatsRevenue | Gross revenue generated through Uber Eats orders |

# | DoorDashRevenue | Gross revenue generated through DoorDash orders |

# | SelfDeliveryRevenue | Gross revenue generated through self-managed delivery orders |

# | COGSRate | Cost of Goods Sold as a percentage of revenue (20%–40%) |

# | OPEXRate | Operating expenses as a percentage of revenue (20%–55%) |

# | CommissionRate | Commission charged by third-party delivery platforms |

# | DeliveryRadiusKM | Maximum delivery distance offered (3–18 km) |

# | DeliveryCostOrder | Fixed cost per self-delivery order ($0.89–$5.31) |

# | SD\_DeliveryTotalCost | Total monthly cost for self-delivery logistics |

# | InStoreNetProfit | Net profit from in-store sales |

# | UberEatsNetProfit | Net profit from Uber Eats orders |

# | DoorDashNetProfit | Net profit from DoorDash orders |

# | SelfDeliveryNetProfit | Net profit from self-delivery orders |

# | InStoreShare | Percentage of total orders that are in-store |

# | UE\_share | Share of delivery orders from Uber Eats |

# | DD\_share | Share of delivery orders from DoorDash |

# | SD\_share | Share of self-delivery orders |

# 

# \---

# 

# \## 📈 Key Performance Indicators (KPIs)

# 

# | KPI Name | Description |

# |----------|-------------|

# | Net Profit per Order | True channel efficiency |

# | Channel Margin (%) | Profitability strength |

# | Commission Drag Index | Margin loss due to aggregators |

# | Self-Delivery ROI | In-house delivery efficiency |

# | Profit Volatility Score | Financial risk indicator |

# 

# \---

# 

# \## 📌 Project Summary

# 

# This project evaluates restaurant profitability across multiple sales channels to identify:

# \- Which channels maximize profit

# \- Where commission costs erode margins

# \- Whether self-delivery is financially viable

# \- How restaurants can optimize channel strategy using data

