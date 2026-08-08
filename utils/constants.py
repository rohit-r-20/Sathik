# Business Verticals
BUSINESSES = [
    {
        'id': 'plumbing',
        'name': 'Plumbing Products',
        'slug': 'plumbing',
        'short_description': 'Pipes, fittings, valves, pumps, and water management solutions from top brands.',
        'icon': '🔧',
        'order': 1
    },
    {
        'id': 'hardware',
        'name': 'Hardware Products',
        'slug': 'hardware',
        'short_description': 'Door fittings, fasteners, tools, safety equipment, and industrial hardware.',
        'icon': '🔨',
        'order': 2
    },
    {
        'id': 'bath-kitchen',
        'name': 'Bath & Kitchen',
        'slug': 'bath-kitchen',
        'short_description': 'Sanitaryware, faucets, showers, bathtubs, kitchen sinks, and accessories.',
        'icon': '🛁',
        'order': 3
    }
]

# Authorized Brands (All official dealers & suppliers for Sathik Traders)
BRANDS_LIST = [
    {'name': 'Jaquar', 'slug': 'jaquar', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Hindware', 'slug': 'hindware', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'CERA', 'slug': 'cera', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Astral Pipes', 'slug': 'astral', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Ashirvad Pipes', 'slug': 'ashirvad', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'C.R.I. Pumps', 'slug': 'cri', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'BOSCH', 'slug': 'bosch', 'businesses': ['hardware'], 'featured': True, 'country': 'Germany / India'},
    {'name': 'SKF Bearings', 'slug': 'skf', 'businesses': ['hardware'], 'featured': True, 'country': 'Sweden / India'},
    {'name': 'V-GUARD', 'slug': 'v-guard', 'businesses': ['plumbing', 'hardware'], 'featured': True, 'country': 'India'},
    {'name': 'ÉSSCO Bath Fittings', 'slug': 'eesco', 'businesses': ['bath-kitchen', 'plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Makita Power Tools', 'slug': 'makita', 'businesses': ['hardware'], 'featured': True, 'country': 'Japan / India'},
    {'name': 'Lubi Pumps & Motors', 'slug': 'lubi', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Parryware', 'slug': 'parryware', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'DeWALT', 'slug': 'dewalt', 'businesses': ['hardware'], 'featured': True, 'country': 'USA / India'},
    {'name': 'Finolex Pipes', 'slug': 'finolex', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'TAPARIA Tools', 'slug': 'taparia', 'businesses': ['hardware'], 'featured': True, 'country': 'India'},
    {'name': 'Legrand Electrical', 'slug': 'legrand', 'businesses': ['hardware'], 'featured': True, 'country': 'France / India'},
    {'name': 'HiKOKI Power Tools', 'slug': 'hikoki', 'businesses': ['hardware'], 'featured': True, 'country': 'Japan / India'},
    {'name': 'EKKI Water Tech', 'slug': 'ekki', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Almaa Pumps', 'slug': 'almaa-pumps', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
    {'name': 'Kore Arc GB', 'slug': 'kore-arc', 'businesses': ['hardware'], 'featured': False, 'country': 'India'},
    {'name': 'Niagara Automations', 'slug': 'niagara-automations', 'businesses': ['hardware'], 'featured': False, 'country': 'India'},
    {'name': 'Fenner Belts', 'slug': 'fenner', 'businesses': ['hardware'], 'featured': False, 'country': 'India'},
    {'name': 'Ramesh Hitechk Pumps', 'slug': 'ramesh-pumps', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
    {'name': 'Aqua Tech Tanks', 'slug': 'aqua-tech', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
    {'name': 'Best Arc Electrodes', 'slug': 'best-arc', 'businesses': ['hardware'], 'featured': False, 'country': 'India'},
    {'name': 'Greenfos Pumps', 'slug': 'greenfos', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
    {'name': 'Star Pipes & Fittings', 'slug': 'star-pipes', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
    {'name': 'RE Rasi Hardware', 'slug': 'rasi', 'businesses': ['hardware'], 'featured': False, 'country': 'India'},
    {'name': 'Supreme Pipes', 'slug': 'supreme', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
    {'name': 'Prince Pipes', 'slug': 'prince', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
]

# Official Sathik Traders Contact & Location Info
COMPANY_INFO = {
    'name': 'Sathik Traders',
    'full_name': 'Sathik Traders (Sathik Groups)',
    'phone': '044-26322644',
    'mobile': '94443 23644',
    'mobile_formatted': '+91 94443 23644',
    'whatsapp': '919444323644',
    'email': 'sathiktradersredhills@gmail.com',
    'email_alt': 'sathik_traders@yahoo.co.in',
    'address': 'No.6, Dharga Street, G.N.T. Road, Redhills, Chennai - 600 052',
    'street': 'No.6, Dharga Street, G.N.T. Road',
    'area': 'Redhills',
    'city': 'Chennai',
    'state': 'Tamil Nadu',
    'pincode': '600 052',
    'website': 'www.sathiktraders.com',
    'hours': 'Mon – Sat, 9:00 AM – 7:30 PM'
}

# MOCK CATEGORIES & SUBCATEGORIES FOR CLIENT PREVIEW
MOCK_CATEGORIES = [
    # Bath & Kitchen Store Categories
    {
        'name': 'Bathware',
        'slug': 'bathware',
        'business_slug': 'bath-kitchen',
        'description': 'Taps, shower systems, sanitary fixtures, lighting, geysers, bathtubs, and bathroom accessories.',
        'icon': '🛁',
        'order': 1
    },
    {
        'name': 'Kitchenware',
        'slug': 'kitchenware',
        'business_slug': 'bath-kitchen',
        'description': 'Stainless steel sinks, kitchen taps, chimneys, hobs, modular baskets, and drain racks.',
        'icon': '🍳',
        'order': 2
    },
    {
        'name': 'Bathroom Hardware & Mirrors',
        'slug': 'bath-hardware-mirrors',
        'business_slug': 'bath-kitchen',
        'description': 'LED touch mirrors, glass partition fittings, soap dispensers, and premium brass accessories.',
        'icon': '🪞',
        'order': 3
    },

    # Plumbing Products Store Categories
    {
        'name': 'Pipes & Tubing',
        'slug': 'pipes',
        'business_slug': 'plumbing',
        'description': 'CPVC, UPVC, SWR, and underground agricultural water pipes.',
        'icon': '🚰',
        'order': 1
    },
    {
        'name': 'Pipe Fittings & Valves',
        'slug': 'pipe-fittings',
        'business_slug': 'plumbing',
        'description': 'Elbows, tees, couplings, ball valves, gate valves, and brass joints.',
        'icon': '🔧',
        'order': 2
    },
    {
        'name': 'Pumps & Motors',
        'slug': 'pumps',
        'business_slug': 'plumbing',
        'description': 'Submersible pumps, monoblock pumps, and automated pressure booster systems.',
        'icon': '⚡',
        'order': 3
    },

    # Hardware Products Store Categories
    {
        'name': 'Door & Cabinet Hardware',
        'slug': 'door-hardware',
        'business_slug': 'hardware',
        'description': 'Mortise door handles, locks, hinges, drawer telescopic channels, and tower bolts.',
        'icon': '🚪',
        'order': 1
    },
    {
        'name': 'Tools & Equipment',
        'slug': 'tools-equipment',
        'business_slug': 'hardware',
        'description': 'Hand tools, cordless power tools, drills, and laser measurement devices.',
        'icon': '🔨',
        'order': 2
    },
    {
        'name': 'Fasteners & Safety Gear',
        'slug': 'fasteners-safety',
        'business_slug': 'hardware',
        'description': 'SS screws, anchor bolts, helmets, safety shoes, and site protection PPE.',
        'icon': '🦺',
        'order': 3
    }
]

MOCK_SUBCATEGORIES = [
    # Bathware Elements
    {'name': 'Taps & Faucets', 'slug': 'taps-faucets', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🚰', 'order': 1},
    {'name': 'Towel Rods & Hooks', 'slug': 'towel-rods-accessories', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🧣', 'order': 2},
    {'name': 'Bathroom Lighting', 'slug': 'bathroom-lighting', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '💡', 'order': 3},
    {'name': 'Water Heaters & Geysers', 'slug': 'water-heaters-geysers', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🔥', 'order': 4},
    {'name': 'Sanitaryware (Closets & Basins)', 'slug': 'sanitaryware-fixtures', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🚽', 'order': 5},
    {'name': 'Showers & Enclosures', 'slug': 'showers-enclosures', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🚿', 'order': 6},
    {'name': 'Bathtubs & Jacuzzis', 'slug': 'bathtubs', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🛁', 'order': 7},

    # Kitchenware Elements
    {'name': 'Kitchen Sinks & Taps', 'slug': 'kitchen-sinks-taps', 'category_slug': 'kitchenware', 'business_slug': 'bath-kitchen', 'icon': '🚰', 'order': 1},
    {'name': 'Modular Kitchen Baskets', 'slug': 'kitchen-baskets', 'category_slug': 'kitchenware', 'business_slug': 'bath-kitchen', 'icon': '🗄️', 'order': 2},
    {'name': 'Kitchen Chimneys & Hobs', 'slug': 'chimneys-hobs', 'category_slug': 'kitchenware', 'business_slug': 'bath-kitchen', 'icon': '💨', 'order': 3},
    {'name': 'Drain Racks & Accessories', 'slug': 'drain-racks', 'category_slug': 'kitchenware', 'business_slug': 'bath-kitchen', 'icon': '🍽️', 'order': 4},

    # Bath Hardware & Mirrors Elements
    {'name': 'LED Touch Mirrors', 'slug': 'led-mirrors', 'category_slug': 'bath-hardware-mirrors', 'business_slug': 'bath-kitchen', 'icon': '🪞', 'order': 1},
    {'name': 'Soap Dispensers & Holders', 'slug': 'soap-dispensers', 'category_slug': 'bath-hardware-mirrors', 'business_slug': 'bath-kitchen', 'icon': '🧴', 'order': 2},
    {'name': 'Glass Partition Fittings', 'slug': 'shower-partitions', 'category_slug': 'bath-hardware-mirrors', 'business_slug': 'bath-kitchen', 'icon': '🚪', 'order': 3},

    # Plumbing Elements
    {'name': 'CPVC Pipes', 'slug': 'cpvc-pipes', 'category_slug': 'pipes', 'business_slug': 'plumbing', 'icon': '🔵', 'order': 1},
    {'name': 'UPVC Pipes', 'slug': 'upvc-pipes', 'category_slug': 'pipes', 'business_slug': 'plumbing', 'icon': '⚪', 'order': 2},
    {'name': 'SWR Drainage Pipes', 'slug': 'swr-pipes', 'category_slug': 'pipes', 'business_slug': 'plumbing', 'icon': '🪠', 'order': 3},
    {'name': 'CPVC & UPVC Fittings', 'slug': 'cpvc-fittings', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'icon': '🔩', 'order': 1},
    {'name': 'Ball & Gate Valves', 'slug': 'valves', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'icon': '🚰', 'order': 2},
    {'name': 'Submersible Pumps', 'slug': 'submersible-pumps', 'category_slug': 'pumps', 'business_slug': 'plumbing', 'icon': '⚡', 'order': 1},
    {'name': 'Pressure Booster Pumps', 'slug': 'booster-pumps', 'category_slug': 'pumps', 'business_slug': 'plumbing', 'icon': '🌊', 'order': 2},

    # Hardware Elements
    {'name': 'Door Handles & Mortise Locks', 'slug': 'door-handles', 'category_slug': 'door-hardware', 'business_slug': 'hardware', 'icon': '🚪', 'order': 1},
    {'name': 'Hinges & Drawer Slides', 'slug': 'hinges-slides', 'category_slug': 'door-hardware', 'business_slug': 'hardware', 'icon': '🔑', 'order': 2},
    {'name': 'Hand Tools & Kits', 'slug': 'hand-tools', 'category_slug': 'tools-equipment', 'business_slug': 'hardware', 'icon': '🔨', 'order': 1},
    {'name': 'Cordless Power Tools', 'slug': 'power-tools', 'category_slug': 'tools-equipment', 'business_slug': 'hardware', 'icon': '⚡', 'order': 2},
    {'name': 'SS Fasteners & Bolts', 'slug': 'screws-bolts', 'category_slug': 'fasteners-safety', 'business_slug': 'hardware', 'icon': '🔩', 'order': 1},
    {'name': 'Site Safety Gear (PPE)', 'slug': 'safety-gear', 'category_slug': 'fasteners-safety', 'business_slug': 'hardware', 'icon': '🦺', 'order': 2}
]

# MOCK SAMPLE PRODUCTS FOR CLIENT PREVIEW
MOCK_PRODUCTS = [
    # --- BATH & KITCHEN: BATHWARE ELEMENTS ---
    {
        '_id': 'p_tap_1',
        'name': 'Jaquar Kubix Prime Single Lever Basin Mixer Tap',
        'slug': 'jaquar-kubix-prime-basin-mixer-tap',
        'sku': 'JAG-TAP-001',
        'description': 'Jaquar Kubix Prime single lever brass basin tap with mirror-shine chrome finish and smooth ceramic disc cartridge for precise hot & cold control.',
        'short_description': 'Premium mirror-chrome single lever basin mixer tap.',
        'features': ['High-purity brass casting', 'Mirror-shine chrome finish', '10-Year manufacturer warranty'],
        'specifications': [{'key': 'Material', 'value': 'Brass'}, {'key': 'Finish', 'value': 'Chrome'}, {'key': 'Category', 'value': 'Taps & Faucets'}],
        'images': [{'url': '/static/images/products/jaquar_basin_mixer.png', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'bathware',
        'subcategory_slug': 'taps-faucets',
        'brand_slug': 'jaquar',
        'brand_name': 'Jaquar',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_towel_1',
        'name': 'Jaquar Continental Stainless Steel Towel Rod (24 inch)',
        'slug': 'jaquar-continental-towel-rod-24-inch',
        'sku': 'JAG-TR-024',
        'description': 'Heavy-duty 24-inch stainless steel towel rod with rust-proof chrome coating. Concealed wall mount design for sleek modern bathrooms.',
        'short_description': '24" rust-proof stainless steel wall-mounted towel rod.',
        'features': ['Grade 304 Stainless Steel', 'Concealed screw wall mounting', 'Rust & humidity resistant'],
        'specifications': [{'key': 'Length', 'value': '24 Inches'}, {'key': 'Material', 'value': 'SS 304'}],
        'images': [{'url': '/static/images/products/jaquar_towel_rod.png', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'bathware',
        'subcategory_slug': 'towel-rods-accessories',
        'brand_slug': 'jaquar',
        'brand_name': 'Jaquar',
        'is_active': True,
        'is_featured': True,
        'is_new': False
    },
    {
        '_id': 'p_light_1',
        'name': 'Jaquar Waterproof Warm White Bathroom Ceiling Downlight 12W',
        'slug': 'jaquar-waterproof-bathroom-light-12w',
        'sku': 'JAG-LGT-12W',
        'description': 'IP65 moisture-proof architectural LED ceiling light designed specifically for shower areas and high-humidity bathroom environments.',
        'short_description': 'IP65 waterproof 12W LED warm white bathroom light.',
        'features': ['IP65 Waterproof rating', 'Glare-free frosted diffuser', 'Long 50,000-hour LED lifespan'],
        'specifications': [{'key': 'Wattage', 'value': '12W'}, {'key': 'IP Rating', 'value': 'IP65 Waterproof'}],
        'images': [{'url': '/static/images/products/jaquar_towel_rod.png', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'bathware',
        'subcategory_slug': 'bathroom-lighting',
        'brand_slug': 'jaquar',
        'brand_name': 'Jaquar',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_heater_1',
        'name': 'Hindware Elena Storage Water Heater Geyser 25L',
        'slug': 'hindware-elena-storage-water-heater-25l',
        'sku': 'HIND-GYS-25L',
        'description': '25-liter energy-efficient 5-star rated storage geyser with glass-lined tank, titanium heating element, and multi-tier safety valve for instant hot water.',
        'short_description': '25-Liter 5-star energy-efficient electric water heater.',
        'features': ['Titanium glass-lined tank', '5-Star BEE energy rating', 'High pressure withstand up to 8 Bar'],
        'specifications': [{'key': 'Capacity', 'value': '25 Liters'}, {'key': 'Rating', 'value': '5 Star BEE'}],
        'images': [{'url': '/static/images/products/hindware_water_heater.png', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'bathware',
        'subcategory_slug': 'water-heaters-geysers',
        'brand_slug': 'hindware',
        'brand_name': 'Hindware',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_wc_1',
        'name': 'Hindware Italian Collection Wall Hung Water Closet',
        'slug': 'hindware-italian-collection-wall-hung-wc',
        'sku': 'HIND-WC-99',
        'description': 'Sleek Italian design rimless wall-hung water closet with soft-close seat cover and water-saving dual flush mechanism.',
        'short_description': 'Rimless wall-hung ceramic closet with dual flush and soft-close seat.',
        'features': ['Rimless hygienic flushing technology', 'Soft-close durable seat cover', 'Germ-block nano glaze coating'],
        'specifications': [{'key': 'Trap Type', 'value': 'P-Trap'}, {'key': 'Glaze', 'value': 'Nano Glaze'}],
        'images': [{'url': '/static/images/products/hindware_wall_hung_wc.png', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'bathware',
        'subcategory_slug': 'sanitaryware-fixtures',
        'brand_slug': 'hindware',
        'brand_name': 'Hindware',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_shower_1',
        'name': 'CERA Overhead Rain Shower Head with 12-inch Arm',
        'slug': 'cera-overhead-rain-shower-head-12-inch',
        'sku': 'CERA-SHW-01',
        'description': 'Ultra-thin square stainless steel rain shower head with rub-clean silicon nozzles and 12-inch wall shower arm.',
        'short_description': 'Stainless steel rain shower head with easy-clean nozzles.',
        'features': ['Rub-clean self-cleaning silicone nozzles', 'SS 304 mirror finish', 'Includes 12-inch heavy shower arm'],
        'specifications': [{'key': 'Dimensions', 'value': '8x8 Inches'}, {'key': 'Type', 'value': 'Rain Shower'}],
        'images': [{'url': '/static/images/products/jaquar_basin_mixer.png', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'bathware',
        'subcategory_slug': 'showers-enclosures',
        'brand_slug': 'cera',
        'brand_name': 'CERA',
        'is_active': True,
        'is_featured': True,
        'is_new': False
    },

    # --- BATH & KITCHEN: KITCHENWARE ELEMENTS ---
    {
        '_id': 'p_sink_1',
        'name': 'CERA Double Bowl Stainless Steel Kitchen Sink',
        'slug': 'cera-double-bowl-stainless-steel-kitchen-sink',
        'sku': 'CERA-SNK-DBL',
        'description': 'Premium 37x18 inch double bowl kitchen sink constructed from grade 304 satin-finished stainless steel with anti-noise rubber dampening pads.',
        'short_description': 'Grade 304 satin finish double bowl kitchen sink.',
        'features': ['Heavy duty 1.2mm SS 304 steel', 'Undercoated sound deadening pads', 'Includes waste coupling strainers'],
        'specifications': [{'key': 'Dimensions', 'value': '37 x 18 x 9 Inches'}, {'key': 'Material', 'value': 'SS 304 Satin'}],
        'images': [{'url': '/static/images/products/cera_kitchen_sink.png', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'kitchenware',
        'subcategory_slug': 'kitchen-sinks-taps',
        'brand_slug': 'cera',
        'brand_name': 'CERA',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_chimb_1',
        'name': 'Hindware Auto-Clean Kitchen Chimney (60 cm)',
        'slug': 'hindware-autoclean-kitchen-chimney-60cm',
        'sku': 'HIND-CHM-60',
        'description': '60 cm touch control auto-clean kitchen chimney with 1200 m³/hr suction power and motion-sensor operation.',
        'short_description': 'Touch & motion control auto-clean kitchen chimney.',
        'features': ['Thermal auto-clean technology', '1200 m3/hr suction power', 'Touch & motion gesture sensor'],
        'specifications': [{'key': 'Size', 'value': '60 cm'}, {'key': 'Suction', 'value': '1200 m³/hr'}],
        'images': [{'url': '/static/images/products/cera_kitchen_sink.png', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'kitchenware',
        'subcategory_slug': 'chimneys-hobs',
        'brand_slug': 'hindware',
        'brand_name': 'Hindware',
        'is_active': True,
        'is_featured': False,
        'is_new': True
    },

    # --- PLUMBING STORE PRODUCTS ---
    {
        '_id': 'p_cpvc_1',
        'name': 'Astral CPVC Pro Pipe SDR 11 (3/4 inch)',
        'slug': 'astral-cpvc-pro-pipe-sdr-11-3-4-inch',
        'sku': 'AST-CPVC-001',
        'description': 'Astral CPVC Pro pipes are high-performance chlorinated polyvinyl chloride pipes designed for hot and cold water distribution. Tested to withstand high pressures up to 82°C.',
        'short_description': 'High-performance CPVC plumbing pipe for hot and cold water distribution.',
        'features': ['Suitable for hot and cold water (up to 82°C)', 'Lead-free & NSF certified', 'Corrosion & chemical resistant'],
        'specifications': [{'key': 'Material', 'value': 'CPVC Pro'}, {'key': 'Size', 'value': '3/4 inch'}],
        'images': [{'url': '/static/images/products/astral_cpvc_pipe.png', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipes',
        'subcategory_slug': 'cpvc-pipes',
        'brand_slug': 'astral',
        'brand_name': 'Astral',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_elbow_1',
        'name': 'Ashirvad FlowGuard Plus CPVC Elbow 90 Degree (1 inch)',
        'slug': 'ashirvad-flowguard-plus-cpvc-elbow-1-inch',
        'sku': 'ASH-FIT-05',
        'description': 'High strength 90 degree CPVC elbow for leak-proof plumbing direction changes. Chemical resistant and certified for drinking water safety.',
        'short_description': '90-degree leak-proof CPVC elbow fitting for clean water supply lines.',
        'features': ['High impact strength', 'Non-toxic drinking water safe', 'Easy solvent cement jointing'],
        'specifications': [{'key': 'Material', 'value': 'CPVC FlowGuard Plus'}, {'key': 'Angle', 'value': '90 Degree'}],
        'images': [{'url': '/static/images/products/astral_cpvc_pipe.png', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'cpvc-fittings',
        'brand_slug': 'ashirvad',
        'brand_name': 'Ashirvad',
        'is_active': True,
        'is_featured': True,
        'is_new': False
    },
    {
        '_id': 'p_valve_1',
        'name': 'EESCO Heavy Duty Brass Ball Valve (1 inch)',
        'slug': 'eesco-heavy-duty-brass-ball-valve-1-inch',
        'sku': 'EES-VLV-01',
        'description': 'Full port forged brass ball valve with chrome-plated brass ball and vinyl lever handle for reliable flow isolation.',
        'short_description': '1" forged brass full-port ball valve for water flow isolation.',
        'features': ['Forged brass construction', 'Full-port flow design', 'Teflon PTFE seat seals'],
        'specifications': [{'key': 'Size', 'value': '1 Inch'}, {'key': 'Material', 'value': 'Forged Brass'}],
        'images': [{'url': '/static/images/products/eesco_door_handle.png', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'valves',
        'brand_slug': 'eesco',
        'brand_name': 'EESCO',
        'is_active': True,
        'is_featured': True,
        'is_new': False
    },
    {
        '_id': 'p_pump_1',
        'name': 'CRI Openwell Submersible Water Pump 1.5 HP',
        'slug': 'cri-openwell-submersible-pump-1-5hp',
        'sku': 'CRI-PMP-15HP',
        'description': 'Single-phase 1.5 HP copper winding openwell submersible pump designed for residential sumps, overhead tanks, and farm irrigation.',
        'short_description': 'High efficiency 1.5 HP openwell submersible pump.',
        'features': ['100% Copper motor winding', 'High discharge head capability', 'Thermal overload protection'],
        'specifications': [{'key': 'Power', 'value': '1.5 HP'}, {'key': 'Type', 'value': 'Openwell Submersible'}],
        'images': [{'url': '/static/images/products/astral_cpvc_pipe.png', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pumps',
        'subcategory_slug': 'submersible-pumps',
        'brand_slug': 'cri',
        'brand_name': 'CRI',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },

    # --- HARDWARE STORE PRODUCTS ---
    {
        '_id': 'p_handle_1',
        'name': 'EESCO Satin Brass Mortise Door Handle Set with Lock',
        'slug': 'eesco-satin-brass-mortise-door-handle-set',
        'sku': 'EES-HND-SET',
        'description': 'Architectural grade solid brass mortise door handle pair complete with 70mm brass cylinder lock and 3 computerized keys.',
        'short_description': 'Solid brass mortise handle set with computerized key cylinder.',
        'features': ['Solid forged brass body', 'Dual action anti-friction latch', '3 Computerized keys included'],
        'specifications': [{'key': 'Finish', 'value': 'Satin Brass'}, {'key': 'Application', 'value': 'Main Entrance Doors'}],
        'images': [{'url': '/static/images/products/eesco_door_handle.png', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'door-hardware',
        'subcategory_slug': 'door-handles',
        'brand_slug': 'eesco',
        'brand_name': 'EESCO',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_ptool_1',
        'name': 'EESCO Professional 18V Cordless Impact Drill Kit',
        'slug': 'eesco-professional-18v-cordless-impact-drill',
        'sku': 'EES-DRILL-18V',
        'description': 'Heavy-duty 18V brushless motor cordless impact drill with 2x 2.0Ah lithium-ion batteries, fast charger, and carrying case.',
        'short_description': '18V cordless brushless impact drill kit with 2 batteries.',
        'features': ['High torque brushless motor', '2x 2.0Ah Li-ion batteries included', 'Variable speed trigger with LED light'],
        'specifications': [{'key': 'Voltage', 'value': '18V'}, {'key': 'Chuck Size', 'value': '13 mm Keyless'}],
        'images': [{'url': '/static/images/products/eesco_cordless_drill.png', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'tools-equipment',
        'subcategory_slug': 'power-tools',
        'brand_slug': 'eesco',
        'brand_name': 'EESCO',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    }
]


