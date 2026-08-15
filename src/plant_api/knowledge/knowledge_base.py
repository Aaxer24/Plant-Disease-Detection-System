"""
Comprehensive knowledge base for potato, tomato and pepper diseases.
Used as RAG context for the AI chatbot to give accurate farming advice.
"""

PLANT_DISEASE_KNOWLEDGE = {
    # ------------------------------------------------------------------ #
    # Pepper
    # ------------------------------------------------------------------ #
    "Pepper__bell___Bacterial_spot": {
        "disease_name": "Pepper Bacterial Spot",
        "scientific_name": "Xanthomonas campestris pv. vesicatoria",
        "description": "Bacterial spot is a common and destructive disease of bell peppers caused by Xanthomonas bacteria. It affects leaves, stems, and fruit, reducing marketable yield.",
        "symptoms": [
            "Small, water-soaked circular spots on leaves that turn dark brown",
            "Spots may have a yellow halo and look greasy",
            "Leaves turn yellow and drop prematurely (defoliation)",
            "Raised, scab-like brown lesions on fruit",
            "Stem lesions can girdle young plants",
        ],
        "causes": [
            "Caused by Xanthomonas campestris pv. vesicatoria bacteria",
            "Spreads via wind-driven rain, overhead irrigation, and splashing water",
            "Enters through wounds, stomata, or hydathodes",
            "Survives on infected seed, plant debris, and volunteer plants",
            "Favoured by warm (24-30°C), humid, rainy weather",
        ],
        "treatment": [
            "Apply copper-based bactericides (bacteria are not controlled by fungicides)",
            "Combine copper with Mancozeb to slow resistance development",
            "Remove and destroy heavily infected plants",
            "Avoid working in fields when foliage is wet (spreads bacteria on hands/tools)",
        ],
        "prevention": [
            "Use certified disease-free seed and transplants",
            "Practice 2-3 year crop rotation away from peppers and tomatoes",
            "Avoid overhead irrigation — use drip irrigation instead",
            "Disinfect stakes, tools and equipment between fields",
            "Plant resistant/tolerant varieties where available",
            "Space plants for good airflow to reduce leaf wetness duration",
        ],
        "recommended_pesticides": [
            {
                "name": "Copper Hydroxide",
                "type": "Bactericide",
                "usage": "Spray every 7-10 days, especially before rain events",
            },
            {
                "name": "Copper + Mancozeb",
                "type": "Bactericide + Fungicide",
                "usage": "Mix as per label, apply preventively every 7 days",
            },
            {
                "name": "Streptomycin sulfate",
                "type": "Bactericide (where permitted)",
                "usage": "Use only where locally approved; follow label rate strictly",
            },
        ],
        "severity": "Moderate to High - can cause significant defoliation and fruit loss in wet seasons",
        "season": "Warm, humid, rainy periods; common in summer plantings",
    },
    "Pepper__bell___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your bell pepper plant appears healthy! Here are some tips to keep it that way and maximize your yield.",
        "symptoms": [
            "Leaves are uniformly green, glossy, and firm",
            "No spots, lesions, or wilting",
            "Sturdy stems and good branching",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular monitoring for early signs of disease or pests",
        ],
        "prevention": [
            "Water at the base, avoid wetting foliage",
            "Maintain balanced fertilization (NPK per soil test)",
            "Stake or cage plants to keep fruit off the ground",
            "Rotate crops and remove plant debris after harvest",
            "Scout weekly for aphids, thrips, and bacterial spot symptoms",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Apply balanced fertilizer at transplanting, side-dress mid-season",
            "Water deeply 1-2 inches per week, more in fruiting stage",
            "Mulch to conserve moisture and suppress weeds",
            "Harvest peppers regularly to encourage continued fruiting",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Potato
    # ------------------------------------------------------------------ #
    "Potato___Early_blight": {
        "disease_name": "Early Blight",
        "scientific_name": "Alternaria solani",
        "description": "Early blight is a common fungal disease of potatoes caused by Alternaria solani. It primarily affects leaves but can also infect stems and tubers.",
        "symptoms": [
            "Dark brown to black circular spots on lower (older) leaves first",
            "Spots have characteristic concentric rings (target-like or bull's-eye pattern)",
            "Yellow halo around the spots",
            "Leaves eventually turn yellow and drop off",
            "Stem lesions appear as dark, elongated spots",
            "Tuber lesions are dark, sunken, and circular with raised borders",
        ],
        "causes": [
            "Caused by the fungus Alternaria solani",
            "Spreads through wind, rain splash, and contaminated equipment",
            "Thrives in warm (24-29°C / 75-84°F) and humid conditions",
            "Overwinters in infected plant debris and soil",
            "Stressed plants (nutrient deficiency, drought) are more susceptible",
        ],
        "treatment": [
            "Apply fungicides like Chlorothalonil, Mancozeb, or Azoxystrobin",
            "Start fungicide applications when symptoms first appear",
            "Spray every 7-10 days during favorable disease conditions",
            "Remove and destroy infected leaves and plant debris",
            "Apply copper-based fungicides as an organic alternative",
            "Use neem oil spray (organic option) as preventive measure",
        ],
        "prevention": [
            "Practice crop rotation (3-4 year rotation away from potatoes and tomatoes)",
            "Use certified disease-free seed potatoes",
            "Plant resistant varieties when available",
            "Maintain adequate plant spacing for good air circulation",
            "Water at the base of plants, avoid overhead irrigation",
            "Mulch around plants to prevent soil splash onto leaves",
            "Keep plants well-fertilized, especially with nitrogen and potassium",
            "Remove and destroy all plant debris after harvest",
        ],
        "recommended_pesticides": [
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Mix 2-3 grams per liter of water, spray every 7-10 days",
            },
            {
                "name": "Chlorothalonil (Daconil)",
                "type": "Fungicide",
                "usage": "Mix as per label, apply preventively every 7-14 days",
            },
            {
                "name": "Azoxystrobin (Amistar)",
                "type": "Systemic Fungicide",
                "usage": "Apply at first sign of disease, repeat every 14 days",
            },
            {
                "name": "Copper Oxychloride",
                "type": "Organic Fungicide",
                "usage": "Mix 3 grams per liter, spray every 7-10 days",
            },
            {
                "name": "Neem Oil",
                "type": "Organic",
                "usage": "Mix 5ml per liter of water, spray weekly as prevention",
            },
        ],
        "severity": "Moderate to High - Can cause 20-50% yield loss if untreated",
        "season": "Most common in warm, humid weather, typically mid to late growing season",
    },
    "Potato___Late_blight": {
        "disease_name": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "description": "Late blight is a devastating disease caused by the water mold Phytophthora infestans. It was responsible for the Irish Potato Famine (1845-1849). It can destroy entire fields within days under favorable conditions.",
        "symptoms": [
            "Water-soaked, pale green to dark spots on leaf tips and edges",
            "White fuzzy mold growth on the underside of leaves (in humid conditions)",
            "Spots rapidly enlarge and turn dark brown to black",
            "Entire leaves and stems can be destroyed very quickly",
            "A distinctive foul smell from rotting tissue",
            "Tubers develop reddish-brown dry rot that extends into the flesh",
            "Under wet conditions, entire plants can collapse within 1-2 weeks",
        ],
        "causes": [
            "Caused by the oomycete (water mold) Phytophthora infestans",
            "Spreads extremely rapidly through wind-blown spores",
            "Thrives in cool (10-25°C / 50-77°F) and wet/humid conditions",
            "Can spread through infected seed potatoes",
            "Rain and fog greatly increase disease spread",
            "Can survive in volunteer potato plants and cull piles",
        ],
        "treatment": [
            "IMMEDIATE ACTION REQUIRED - Late blight spreads very fast!",
            "Apply systemic fungicides like Metalaxyl (Ridomil) or Cymoxanil",
            "Use contact fungicides like Mancozeb in combination with systemics",
            "Spray every 5-7 days during active disease",
            "Remove and destroy ALL infected plants immediately",
            "Do NOT compost infected material - burn or bury deeply",
            "Harvest tubers as soon as possible from infected fields",
            "Apply phosphorous acid-based products (e.g., Agri-Fos)",
        ],
        "prevention": [
            "Use certified disease-free seed potatoes ALWAYS",
            "Plant resistant varieties (very important for late blight)",
            "Apply preventive fungicides before disease appears during high-risk periods",
            "Monitor weather forecasts - cool, wet weather increases risk",
            "Maintain good field drainage to reduce humidity",
            "Destroy all volunteer potato plants and cull piles",
            "Practice crop rotation (minimum 3 years)",
            "Hill potatoes well to protect tubers from spore wash",
            "Avoid overhead irrigation",
            "Scout fields regularly, especially during cool, wet weather",
        ],
        "recommended_pesticides": [
            {
                "name": "Metalaxyl + Mancozeb (Ridomil Gold)",
                "type": "Systemic + Contact Fungicide",
                "usage": "Mix 2.5g per liter, apply every 7 days during high risk",
            },
            {
                "name": "Cymoxanil + Mancozeb (Curzate)",
                "type": "Systemic + Contact Fungicide",
                "usage": "Mix as per label, apply every 5-7 days",
            },
            {
                "name": "Dimethomorph (Acrobat)",
                "type": "Systemic Fungicide",
                "usage": "Apply preventively or at first symptoms",
            },
            {
                "name": "Mandipropamid (Revus)",
                "type": "Systemic Fungicide",
                "usage": "Apply every 7-10 days as prevention",
            },
            {
                "name": "Copper Hydroxide",
                "type": "Organic Fungicide",
                "usage": "Mix 2-3g per liter, spray every 5-7 days",
            },
            {
                "name": "Phosphorous Acid (Agri-Fos)",
                "type": "Systemic",
                "usage": "Apply as foliar spray or soil drench",
            },
        ],
        "severity": "VERY HIGH - Can cause 100% crop loss if not treated immediately!",
        "season": "Most dangerous in cool, wet conditions - spring and fall in temperate regions",
    },
    "Potato___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your potato plant appears healthy! Here are some tips to keep it that way and maximize your yield.",
        "symptoms": [
            "Leaves are uniformly green and firm",
            "No spots, discoloration, or wilting",
            "Strong, sturdy stems",
            "Good overall plant vigor",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular monitoring for any signs of disease",
            "Maintain your current farming practices",
        ],
        "prevention": [
            "Continue regular crop scouting (check plants weekly)",
            "Maintain balanced fertilization (NPK as per soil test)",
            "Water consistently but avoid overwatering",
            "Practice crop rotation to prevent disease buildup",
            "Use certified disease-free seed potatoes",
            "Keep fields clean of debris and weeds",
            "Monitor weather conditions for disease-favorable periods",
            "Apply preventive fungicides during high-risk weather",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Apply balanced fertilizer (NPK 10-10-20 or similar) at planting",
            "Side-dress with nitrogen 3-4 weeks after emergence",
            "Hill plants when they are 6-8 inches tall to protect tubers",
            "Water deeply but infrequently (1-2 inches per week)",
            "Mulch between rows to conserve moisture and suppress weeds",
            "Monitor for insect pests like Colorado potato beetle and aphids",
            "Harvest when plant tops begin to die back naturally",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Tomato
    # ------------------------------------------------------------------ #
    "Tomato_Bacterial_spot": {
        "disease_name": "Tomato Bacterial Spot",
        "scientific_name": "Xanthomonas spp.",
        "description": "Bacterial spot causes small dark lesions on tomato leaves, stems and fruit, reducing both yield and fruit quality.",
        "symptoms": [
            "Small, water-soaked spots on leaves that turn dark brown to black",
            "Spots may merge, causing large necrotic areas and leaf drop",
            "Raised, scabby brown spots with a greasy halo on fruit",
            "Defoliation exposes fruit to sunscald",
        ],
        "causes": [
            "Caused by Xanthomonas bacteria species",
            "Spread by splashing rain, overhead irrigation, and contaminated tools/hands",
            "Enters through wounds and natural openings",
            "Favoured by warm, wet, humid weather",
            "Survives on infected seed and plant debris",
        ],
        "treatment": [
            "Apply copper-based bactericides, ideally mixed with Mancozeb",
            "Remove and destroy severely infected plants and debris",
            "Avoid handling wet plants to prevent spreading bacteria",
        ],
        "prevention": [
            "Use certified disease-free seed and transplants",
            "Rotate crops for at least 2 years away from tomatoes/peppers",
            "Use drip irrigation instead of overhead sprinklers",
            "Stake/cage plants for better airflow",
            "Disinfect tools and stakes between uses",
        ],
        "recommended_pesticides": [
            {
                "name": "Copper Hydroxide",
                "type": "Bactericide",
                "usage": "Spray every 7-10 days, more often in wet weather",
            },
            {
                "name": "Copper + Mancozeb",
                "type": "Bactericide + Fungicide",
                "usage": "Apply preventively every 7 days",
            },
        ],
        "severity": "Moderate to High - significant yield and fruit-quality loss in wet seasons",
        "season": "Warm, humid, rainy weather",
    },
    "Tomato_Early_blight": {
        "disease_name": "Tomato Early Blight",
        "scientific_name": "Alternaria solani / A. tomatophila",
        "description": "Early blight is one of the most common fungal diseases of tomato, causing leaf spots and defoliation that reduce yield and fruit quality.",
        "symptoms": [
            "Dark brown spots with concentric rings (target/bull's-eye pattern) on older leaves first",
            "Yellowing of tissue surrounding spots",
            "Progressive defoliation from the bottom of the plant upward",
            "Dark, sunken lesions can also appear on stems and fruit near the stem end",
        ],
        "causes": [
            "Caused by Alternaria fungi",
            "Spread by wind, rain splash, and contaminated tools",
            "Favoured by warm temperatures and high humidity/leaf wetness",
            "Overwinters in plant debris and soil",
            "Stressed or nutrient-deficient plants are more susceptible",
        ],
        "treatment": [
            "Apply fungicides such as Chlorothalonil, Mancozeb, or Azoxystrobin at first symptoms",
            "Repeat every 7-10 days during favorable conditions",
            "Remove and destroy infected lower leaves",
            "Use copper-based fungicide or neem oil as organic options",
        ],
        "prevention": [
            "Rotate crops (avoid tomato/potato for 2-3 years)",
            "Stake and prune plants for airflow, mulch to reduce soil splash",
            "Water at the base, avoid overhead irrigation",
            "Choose resistant varieties where available",
            "Remove plant debris at end of season",
        ],
        "recommended_pesticides": [
            {
                "name": "Chlorothalonil",
                "type": "Fungicide",
                "usage": "Apply preventively every 7-14 days",
            },
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Mix 2-3g per liter, spray every 7-10 days",
            },
            {
                "name": "Azoxystrobin",
                "type": "Systemic Fungicide",
                "usage": "Apply at first sign of disease, repeat every 14 days",
            },
            {"name": "Copper Fungicide", "type": "Organic", "usage": "Spray every 7-10 days"},
        ],
        "severity": "Moderate to High - can cause substantial defoliation and yield loss",
        "season": "Warm, humid weather; mid-to-late season",
    },
    "Tomato_Late_blight": {
        "disease_name": "Tomato Late Blight",
        "scientific_name": "Phytophthora infestans",
        "description": "The same pathogen that causes potato late blight; it can devastate tomato crops within days under cool, wet conditions.",
        "symptoms": [
            "Water-soaked, irregular pale-green to brown lesions on leaves, often starting at leaf edges",
            "White fuzzy fungal growth on leaf undersides in humid conditions",
            "Rapid blackening and collapse of foliage and stems",
            "Firm, brown, greasy-looking lesions on fruit that can rot quickly",
        ],
        "causes": [
            "Caused by the oomycete Phytophthora infestans",
            "Spreads rapidly via wind-blown spores over long distances",
            "Thrives in cool, wet, humid weather",
            "Can spread from nearby infected potato crops",
        ],
        "treatment": [
            "IMMEDIATE ACTION REQUIRED - spreads extremely fast",
            "Apply systemic fungicides (Metalaxyl, Cymoxanil) combined with a contact fungicide like Mancozeb",
            "Spray every 5-7 days during active outbreaks",
            "Remove and destroy infected plants immediately - do not compost",
        ],
        "prevention": [
            "Plant resistant/tolerant varieties",
            "Avoid planting near potato fields",
            "Improve airflow via staking/pruning, avoid overhead irrigation",
            "Monitor weather - cool, wet forecasts mean high risk",
            "Apply preventive fungicide sprays ahead of high-risk periods",
        ],
        "recommended_pesticides": [
            {
                "name": "Metalaxyl + Mancozeb",
                "type": "Systemic + Contact Fungicide",
                "usage": "Apply every 7 days during high risk periods",
            },
            {
                "name": "Cymoxanil + Mancozeb (Curzate)",
                "type": "Systemic + Contact Fungicide",
                "usage": "Apply every 5-7 days",
            },
            {
                "name": "Chlorothalonil",
                "type": "Contact Fungicide",
                "usage": "Apply preventively every 7 days",
            },
        ],
        "severity": "VERY HIGH - can destroy entire crop within days if untreated",
        "season": "Cool, wet weather - typically early spring or fall",
    },
    "Tomato_Leaf_Mold": {
        "disease_name": "Tomato Leaf Mold",
        "scientific_name": "Passalora fulva (syn. Fulvia fulva / Cladosporium fulvum)",
        "description": "Leaf mold is a fungal disease especially problematic in greenhouse and high-humidity tomato production, affecting foliage and reducing photosynthesis.",
        "symptoms": [
            "Pale green to yellow spots on the upper leaf surface",
            "Olive-green to grayish-purple velvety mold on the corresponding leaf underside",
            "Leaves curl, wither, and drop as the disease progresses",
            "Rarely affects fruit directly",
        ],
        "causes": [
            "Caused by the fungus Passalora fulva",
            "Favoured by high humidity (>85%) and moderate temperatures",
            "Very common in greenhouses/polytunnels with poor ventilation",
            "Spreads via airborne spores and water splash",
        ],
        "treatment": [
            "Improve ventilation and reduce humidity immediately",
            "Apply fungicides such as Chlorothalonil, Mancozeb, or Copper-based products",
            "Remove and destroy heavily infected leaves",
        ],
        "prevention": [
            "Ventilate greenhouses well; use fans to reduce leaf wetness",
            "Space plants properly and prune for airflow",
            "Water at the base early in the day so foliage dries quickly",
            "Choose resistant varieties where available",
            "Sanitize greenhouse structures between seasons",
        ],
        "recommended_pesticides": [
            {
                "name": "Chlorothalonil",
                "type": "Fungicide",
                "usage": "Apply every 7-10 days during high humidity periods",
            },
            {"name": "Copper Fungicide", "type": "Organic", "usage": "Spray every 7-10 days"},
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Apply as per label every 7-10 days",
            },
        ],
        "severity": "Moderate - mainly a greenhouse problem, reduces yield through leaf loss",
        "season": "High humidity conditions, common in greenhouse production year-round",
    },
    "Tomato_Septoria_leaf_spot": {
        "disease_name": "Tomato Septoria Leaf Spot",
        "scientific_name": "Septoria lycopersici",
        "description": "Septoria leaf spot is a widespread fungal disease that causes progressive defoliation starting from the lower leaves, weakening the plant and exposing fruit to sunscald.",
        "symptoms": [
            "Small, circular spots with dark brown margins and gray/tan centers on lower leaves first",
            "Tiny black fruiting bodies (pycnidia) visible in the center of older spots",
            "Severe infections cause yellowing and dropping of leaves from the bottom up",
            "Rarely affects fruit",
        ],
        "causes": [
            "Caused by the fungus Septoria lycopersici",
            "Spreads via rain splash, overhead irrigation, and contaminated tools",
            "Favoured by warm, wet weather and prolonged leaf wetness",
            "Overwinters in plant debris and on volunteer tomato plants",
        ],
        "treatment": [
            "Apply fungicides (Chlorothalonil, Mancozeb, Copper) at first sign of spots",
            "Repeat every 7-10 days, especially in wet weather",
            "Remove and destroy infected lower leaves promptly",
        ],
        "prevention": [
            "Rotate crops away from tomato/potato for 2-3 years",
            "Mulch to prevent soil splash onto lower leaves",
            "Stake/prune for airflow, water at the base",
            "Remove volunteer tomato plants and clean up debris after harvest",
        ],
        "recommended_pesticides": [
            {
                "name": "Chlorothalonil",
                "type": "Fungicide",
                "usage": "Apply preventively every 7-10 days",
            },
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Mix 2-3g per liter, spray every 7-10 days",
            },
            {"name": "Copper Fungicide", "type": "Organic", "usage": "Spray every 7-10 days"},
        ],
        "severity": "Moderate to High - progressive defoliation can significantly reduce yield",
        "season": "Warm, wet weather; common mid-to-late season",
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "disease_name": "Two-Spotted Spider Mite Damage",
        "scientific_name": "Tetranychus urticae",
        "description": "Not a disease but a pest infestation — tiny spider mites feed on leaf undersides, causing stippling and, in heavy infestations, webbing and plant decline.",
        "symptoms": [
            "Fine yellow/white stippling (tiny dots) on leaf upper surfaces",
            "Leaves appear bronzed, speckled, or dusty",
            "Fine webbing visible on leaf undersides and between stems in heavy infestations",
            "Leaves may yellow, dry out, and drop in severe cases",
        ],
        "causes": [
            "Caused by Tetranychus urticae, a tiny sap-sucking arachnid (not an insect)",
            "Thrives in hot, dry, dusty conditions",
            "Populations explode rapidly in drought-stressed plants",
            "Spreads by wind, on clothing/tools, and from nearby infested plants",
        ],
        "treatment": [
            "Spray plants (including leaf undersides) with water to dislodge mites",
            "Apply insecticidal soap or horticultural oil, targeting leaf undersides",
            "Use miticides (e.g., Abamectin, Bifenazate) for severe infestations",
            "Introduce natural predators like predatory mites (Phytoseiulus persimilis) or ladybugs",
        ],
        "prevention": [
            "Avoid drought stress - maintain consistent watering",
            "Reduce dust around plants (mites thrive in dusty conditions)",
            "Avoid excessive nitrogen fertilization which favors mite reproduction",
            "Monitor regularly, especially in hot, dry weather",
            "Encourage beneficial predatory insects/mites in the garden",
        ],
        "recommended_pesticides": [
            {
                "name": "Insecticidal Soap",
                "type": "Contact / Organic",
                "usage": "Spray thoroughly on leaf undersides every 5-7 days",
            },
            {
                "name": "Horticultural Oil (Neem/Mineral)",
                "type": "Contact / Organic",
                "usage": "Apply every 7 days, avoid spraying in direct sun/heat",
            },
            {
                "name": "Abamectin",
                "type": "Miticide",
                "usage": "Apply per label for severe infestations, rotate with other modes of action",
            },
        ],
        "severity": "Moderate to High in hot/dry conditions - can weaken plants and reduce yield",
        "season": "Hot, dry weather - most problematic in summer",
    },
    "Tomato__Target_Spot": {
        "disease_name": "Tomato Target Spot",
        "scientific_name": "Corynespora cassiicola",
        "description": "Target spot is a fungal disease causing leaf, stem and fruit lesions with a distinctive target-like pattern, capable of rapid defoliation in warm, humid climates.",
        "symptoms": [
            "Small water-soaked spots that enlarge into brown lesions with concentric rings",
            "Lesions can merge causing large necrotic patches and severe defoliation",
            "Sunken, dark lesions on fruit with concentric ring patterns",
            "Stem lesions can girdle young growth",
        ],
        "causes": [
            "Caused by the fungus Corynespora cassiicola",
            "Favoured by warm temperatures and high humidity/extended leaf wetness",
            "Spreads via wind-blown spores and water splash",
            "Survives in plant debris between seasons",
        ],
        "treatment": [
            "Apply fungicides such as Azoxystrobin, Chlorothalonil, or Mancozeb",
            "Begin applications at first sign of disease, repeat every 7-10 days",
            "Remove and destroy heavily infected leaves and fruit",
        ],
        "prevention": [
            "Rotate crops away from tomato for 1-2 years",
            "Improve airflow through staking/pruning and proper spacing",
            "Avoid overhead irrigation, water at the base",
            "Remove crop debris after harvest",
        ],
        "recommended_pesticides": [
            {
                "name": "Azoxystrobin",
                "type": "Systemic Fungicide",
                "usage": "Apply at first symptoms, repeat every 14 days",
            },
            {
                "name": "Chlorothalonil",
                "type": "Fungicide",
                "usage": "Apply preventively every 7-10 days",
            },
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Mix 2-3g per liter, spray every 7-10 days",
            },
        ],
        "severity": "Moderate to High - can cause rapid defoliation in favorable conditions",
        "season": "Warm, humid weather; common in tropical/subtropical growing regions",
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "disease_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "scientific_name": "Tomato yellow leaf curl virus (Begomovirus)",
        "description": "TYLCV is a devastating viral disease transmitted by whiteflies. Infection early in plant development can cause near-total yield loss.",
        "symptoms": [
            "Severe upward curling and crumpling of leaves",
            "Marked yellowing (chlorosis) of leaf margins and interveinal areas",
            "Stunted, bushy plant growth with shortened internodes",
            "Flower drop and drastically reduced fruit set",
        ],
        "causes": [
            "Caused by a Begomovirus transmitted exclusively by the whitefly Bemisia tabaci",
            "Not spread mechanically (not by touch/tools) - whitefly transmission only",
            "Whitefly populations build up rapidly in warm weather",
            "Weeds and other crops can act as a virus reservoir between seasons",
        ],
        "treatment": [
            "There is NO cure once a plant is infected - focus on whitefly control and removal",
            "Remove and destroy infected plants immediately to reduce virus reservoir",
            "Control whitefly vectors with insecticidal soap, neem oil, or systemic insecticides (Imidacloprid)",
            "Use yellow sticky traps to monitor and reduce whitefly populations",
        ],
        "prevention": [
            "Plant TYLCV-resistant/tolerant tomato varieties",
            "Use reflective mulches to repel whiteflies",
            "Install fine mesh screens/row covers on seedlings and young transplants",
            "Control weeds that host whiteflies around the field",
            "Avoid planting new tomatoes near existing infected plantings",
            "Manage whitefly populations proactively before symptoms appear",
        ],
        "recommended_pesticides": [
            {
                "name": "Imidacloprid",
                "type": "Systemic Insecticide (whitefly control)",
                "usage": "Apply as soil drench at transplanting per label",
            },
            {
                "name": "Insecticidal Soap",
                "type": "Contact / Organic",
                "usage": "Spray on leaf undersides to reduce whitefly nymphs",
            },
            {
                "name": "Neem Oil",
                "type": "Organic",
                "usage": "Apply every 7 days to disrupt whitefly life cycle",
            },
        ],
        "severity": "VERY HIGH - can cause up to 100% yield loss if plants are infected young",
        "season": "Warm weather when whitefly populations are high, typically summer",
    },
    "Tomato__Tomato_mosaic_virus": {
        "disease_name": "Tomato Mosaic Virus (ToMV)",
        "scientific_name": "Tomato mosaic virus",
        "description": "ToMV is a highly stable and easily spread virus causing mottling and distortion of leaves and fruit, reducing yield and quality.",
        "symptoms": [
            "Light and dark green mottled/mosaic pattern on leaves",
            "Leaf distortion - narrowing, curling, or fern-like leaves",
            "Stunted plant growth",
            "Internal browning or mottling of fruit; uneven ripening",
        ],
        "causes": [
            "Caused by Tomato mosaic virus, extremely stable and long-lived in plant debris and soil",
            "Spreads mechanically through handling, tools, and contaminated hands/clothing",
            "Can be seed-borne",
            "Does NOT require an insect vector - human handling is the main spread route",
        ],
        "treatment": [
            "There is NO cure - remove and destroy infected plants immediately",
            "Wash hands and disinfect tools thoroughly after handling infected plants",
            "Avoid handling plants while smoking/using tobacco products (virus can be present in tobacco)",
        ],
        "prevention": [
            "Use certified virus-free seed, or treat seed as recommended",
            "Plant resistant varieties (Tm resistance genes) where available",
            "Disinfect tools, stakes and hands between plants (10% bleach or trisodium phosphate solution)",
            "Avoid working with tomato plants after handling tobacco products",
            "Remove and destroy all infected plant debris - do not compost",
            "Rotate crops and control weeds that may harbor the virus",
        ],
        "recommended_pesticides": [],
        "severity": "High - reduces yield and fruit quality, no chemical treatment available",
        "season": "Can occur any time; spread accelerated by frequent handling (pruning, tying, harvesting)",
    },
    "Tomato_healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your tomato plant appears healthy! Here are some tips to keep it that way and maximize your yield.",
        "symptoms": [
            "Leaves are uniformly green and firm",
            "No spots, mottling, curling, or wilting",
            "Strong stems with good branching and flowering",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular monitoring for early signs of disease or pests",
        ],
        "prevention": [
            "Water at the base early in the day, avoid wetting foliage",
            "Stake/cage plants and prune for good airflow",
            "Maintain balanced fertilization (NPK per soil test)",
            "Rotate crops and remove plant debris after harvest",
            "Scout weekly for whiteflies, spider mites, and early leaf-spot symptoms",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Apply balanced fertilizer at transplanting, side-dress during fruiting",
            "Water deeply and consistently - 1-2 inches per week",
            "Mulch to conserve moisture and reduce soil splash onto leaves",
            "Remove suckers and lower leaves touching the soil",
            "Harvest regularly to encourage continued fruit production",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
}


def get_disease_context(disease_class: str) -> str:
    """Generate a comprehensive context string for the RAG chatbot."""
    info = PLANT_DISEASE_KNOWLEDGE.get(disease_class)
    if not info:
        return "No information available for this classification."

    context_parts = [
        f"## Disease Detected: {info['disease_name']}",
        f"**Scientific Name:** {info.get('scientific_name', 'N/A')}",
        f"\n**Description:** {info['description']}",
    ]

    if info.get("symptoms"):
        context_parts.append("\n**Symptoms:**")
        for s in info["symptoms"]:
            context_parts.append(f"- {s}")

    if info.get("causes"):
        context_parts.append("\n**Causes:**")
        for c in info["causes"]:
            context_parts.append(f"- {c}")

    if info.get("treatment"):
        context_parts.append("\n**Treatment:**")
        for t in info["treatment"]:
            context_parts.append(f"- {t}")

    if info.get("prevention"):
        context_parts.append("\n**Prevention:**")
        for p in info["prevention"]:
            context_parts.append(f"- {p}")

    if info.get("recommended_pesticides"):
        context_parts.append("\n**Recommended Pesticides/Fungicides:**")
        for pest in info["recommended_pesticides"]:
            context_parts.append(f"- **{pest['name']}** ({pest['type']}): {pest['usage']}")

    if info.get("care_tips"):
        context_parts.append("\n**Care Tips:**")
        for tip in info["care_tips"]:
            context_parts.append(f"- {tip}")

    context_parts.append(f"\n**Severity:** {info.get('severity', 'Unknown')}")
    context_parts.append(f"**Season:** {info.get('season', 'Unknown')}")

    return "\n".join(context_parts)
