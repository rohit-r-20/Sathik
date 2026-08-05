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

# Authorized Brands
BRANDS_LIST = [
    {'name': 'Jaquar', 'slug': 'jaquar', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Hindware', 'slug': 'hindware', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'CERA', 'slug': 'cera', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Astral', 'slug': 'astral', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Ashirvad', 'slug': 'ashirvad', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Supreme', 'slug': 'supreme', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
    {'name': 'Prince', 'slug': 'prince', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
    {'name': 'CRI', 'slug': 'cri', 'businesses': ['plumbing'], 'featured': False, 'country': 'India'},
    {'name': 'EESCO', 'slug': 'eesco', 'businesses': ['plumbing', 'hardware'], 'featured': False, 'country': 'India'},
]

# Contact info
COMPANY_INFO = {
    'name': 'Sathik Groups',
    'phone': '+91 99999 99999',
    'whatsapp': '919999999999',
    'email': 'info@sathikgroups.com',
    'address': 'Your City, State, India',
    'hours': 'Mon – Sat, 9:00 AM – 7:00 PM'
}

# MOCK CATEGORIES & SUBCATEGORIES FOR CLIENT PREVIEW
MOCK_CATEGORIES = [
    {'name': 'Pipes', 'slug': 'pipes', 'business_slug': 'plumbing', 'order': 1},
    {'name': 'Pipe Fittings', 'slug': 'pipe-fittings', 'business_slug': 'plumbing', 'order': 2},
    {'name': 'Sanitaryware', 'slug': 'sanitaryware', 'business_slug': 'bath-kitchen', 'order': 1},
    {'name': 'Faucets & Mixers', 'slug': 'faucets-mixers', 'business_slug': 'bath-kitchen', 'order': 2},
]

# MOCK SAMPLE PRODUCTS FOR CLIENT PREVIEW
MOCK_PRODUCTS = [
    {
        '_id': 'p1',
        'name': 'Astral CPVC Pro Pipe SDR 11 (3/4 inch)',
        'slug': 'astral-cpvc-pro-pipe-sdr-11-3-4-inch',
        'sku': 'AST-CPVC-001',
        'description': 'Astral CPVC Pro pipes are high-performance chlorinated polyvinyl chloride pipes designed for hot and cold water distribution. Tested to withstand high pressures up to 82°C.',
        'short_description': 'High-performance CPVC plumbing pipe for hot and cold water distribution.',
        'features': ['Suitable for hot and cold water (up to 82°C)', 'Lead-free & NSF certified', 'Corrosion & chemical resistant', 'Smooth inner surface for low friction'],
        'specifications': [
            {'key': 'Material', 'value': 'CPVC Pro'},
            {'key': 'Size', 'value': '3/4 inch'},
            {'key': 'Standard', 'value': 'ASTM D2846'}
        ],
        'images': [{'url': '/static/images/placeholder.jpg', 'is_primary': True}],
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
        '_id': 'p2',
        'name': 'Jaquar Single Lever Basin Mixer (Kubix Prime)',
        'slug': 'jaquar-single-lever-basin-mixer-kubix-prime',
        'sku': 'JAG-KUB-01',
        'description': 'Jaquar Kubix Prime single lever basin mixer with 450mm flexible hose. Crafted with high-purity brass for superior durability and finished in mirror-shine chrome.',
        'short_description': 'Premium brass basin mixer with mirror-shine chrome finish and smooth ceramic cartridge.',
        'features': ['High purity brass casting', 'Mirror-shine chrome plating', 'Advanced smooth ceramic cartridge', '10 years warranty'],
        'specifications': [
            {'key': 'Finish', 'value': 'Chrome'},
            {'key': 'Mount Type', 'value': 'Deck Mount'},
            {'key': 'Warranty', 'value': '10 Years'}
        ],
        'images': [{'url': '/static/images/placeholder.jpg', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'faucets-mixers',
        'subcategory_slug': 'basin-mixers',
        'brand_slug': 'jaquar',
        'brand_name': 'Jaquar',
        'is_active': True,
        'is_featured': True,
        'is_new': False
    },
    {
        '_id': 'p3',
        'name': 'Hindware Italian Collection Wall Hung Water Closet',
        'slug': 'hindware-italian-collection-wall-hung-wc',
        'sku': 'HIND-WC-99',
        'description': 'Sleek Italian design rimless wall-hung water closet with soft-close seat cover and water-saving dual flush mechanism.',
        'short_description': 'Rimless wall-hung ceramic closet with dual flush and soft-close seat.',
        'features': ['Rimless hygienic flushing technology', 'Soft-close durable seat cover', 'Germ-block nano glaze coating'],
        'specifications': [
            {'key': 'Trap Type', 'value': 'P-Trap'},
            {'key': 'Glaze', 'value': 'Nano Glaze'},
            {'key': 'Color', 'value': 'White'}
        ],
        'images': [{'url': '/static/images/placeholder.jpg', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'sanitaryware',
        'subcategory_slug': 'water-closets',
        'brand_slug': 'hindware',
        'brand_name': 'Hindware',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p4',
        'name': 'Ashirvad FlowGuard Plus CPVC Elbow 90 Degree (1 inch)',
        'slug': 'ashirvad-flowguard-plus-cpvc-elbow-1-inch',
        'sku': 'ASH-FIT-05',
        'description': 'High strength 90 degree CPVC elbow for leak-proof plumbing direction changes. Chemical resistant and certified for drinking water safety.',
        'short_description': '90-degree leak-proof CPVC elbow fitting for clean water supply lines.',
        'features': ['High impact strength', 'Non-toxic drinking water safe', 'Easy solvent cement jointing'],
        'specifications': [
            {'key': 'Material', 'value': 'CPVC FlowGuard Plus'},
            {'key': 'Angle', 'value': '90 Degree'},
            {'key': 'Size', 'value': '1 inch'}
        ],
        'images': [{'url': '/static/images/placeholder.jpg', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'cpvc-fittings',
        'brand_slug': 'ashirvad',
        'brand_name': 'Ashirvad',
        'is_active': True,
        'is_featured': True,
        'is_new': False
    }
]
