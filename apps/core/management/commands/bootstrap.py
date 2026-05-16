from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from apps.products.models import Category, Product
from apps.core.models import PageContent
from apps.cms.models import ContentBlock, HeroSlide


class Command(BaseCommand):
    help = 'Bootstrap Biochem with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating categories...')
        cat_juice, _ = Category.objects.get_or_create(
            slug='fruit-juices',
            defaults={
                'name': 'Fruit Juices',
                'name_ru': 'Фруктовые соки',
                'name_uz': 'Mevali sharbatlari',
                'description': 'Pure, refreshing juices made from the finest fruits.',
                'description_ru': 'Чистые, освежающие соки из лучших фруктов.',
                'description_uz': 'Eng sifatli mevalardan tayyorlangan toza, tetiklashtiruvchi sharbatlar.',
                'order': 1,
            }
        )
        cat_nectar, _ = Category.objects.get_or_create(
            slug='nectars',
            defaults={
                'name': 'Nectars',
                'name_ru': 'Нектары',
                'name_uz': 'Nektarlar',
                'description': 'Rich nectars with a velvety texture.',
                'description_ru': 'Насыщенные нектары с бархатной текстурой.',
                'description_uz': 'Yumshoq tuzilishga ega boy nektarlar.',
                'order': 2,
            }
        )
        cat_preserve, _ = Category.objects.get_or_create(
            slug='preserves',
            defaults={
                'name': 'Preserves',
                'name_ru': 'Консервы',
                'name_uz': 'Konservalar',
                'description': 'Timeless fruit preserves and jams.',
                'description_ru': 'Вневременные фруктовые джемы и варенья.',
                'description_uz': "Qadrdon meva murabbo va djemlar.",
                'order': 3,
            }
        )

        self.stdout.write('Creating products...')
        products_data = [
            {
                'slug': 'apple-juice-1l',
                'category': cat_juice,
                'name': 'Apple Juice 1L',
                'name_ru': 'Яблочный сок 1л',
                'name_uz': "Olma sharbatlari 1l",
                'tagline': 'Made with 100% real fruit',
                'tagline_ru': 'Из 100% натуральных фруктов',
                'tagline_uz': '100% tabiiy mevalardan',
                'description': 'Crisp, refreshing apple juice pressed from hand-picked orchard apples. No added sugar, no preservatives.',
                'description_ru': 'Освежающий яблочный сок, отжатый из собранных вручную садовых яблок. Без добавления сахара и консервантов.',
                'description_uz': "Qo'lda terilgan bog' olmalaridan siqilgan tetiklashtiruvchi olma sharbatlari. Qo'shimcha shakar va konservansiz.",
                'ingredients': 'Apple juice, vitamin C.',
                'ingredients_ru': 'Яблочный сок, витамин C.',
                'ingredients_uz': 'Olma sharbati, C vitamini.',
                'nutrition_facts': 'Per 100ml: Energy 46kcal, Protein 0.1g, Carbohydrates 11g, Fat 0g.',
                'nutrition_facts_ru': 'На 100 мл: Энергия 46 ккал, Белки 0,1 г, Углеводы 11 г, Жиры 0 г.',
                'nutrition_facts_uz': "100 ml ga: Energiya 46 kkal, Oqsillar 0,1 g, Uglevodlar 11 g, Yog'lar 0 g.",
                'weight_grams': 1000,
                'is_featured': True,
            },
            {
                'slug': 'peach-nectar-500ml',
                'category': cat_nectar,
                'name': 'Peach Nectar 0.5L',
                'name_ru': 'Персиковый нектар 0.5л',
                'name_uz': 'Shaftoli nektari 0.5l',
                'tagline': 'Velvety smooth texture',
                'tagline_ru': 'Бархатная гладкая текстура',
                'tagline_uz': 'Yumshoq, silliq tuzilishi',
                'description': 'Sun-ripened peaches blended into a rich, velvety nectar.',
                'description_ru': 'Созревшие на солнце персики, превращенные в насыщенный бархатный нектар.',
                'description_uz': "Quyoshda pishgan shaftolilardan boy, yumshoq nektar. Qo'shimcha shakarsiz.",
                'ingredients': 'Peach puree, water, sugar, citric acid.',
                'ingredients_ru': 'Персиковое пюре, вода, сахар, лимонная кислота.',
                'ingredients_uz': "Shaftoli pyuresi, suv, shakar, limon kislotasi.",
                'nutrition_facts': 'Per 100ml: Energy 54kcal, Protein 0.2g, Carbohydrates 13g, Fat 0g.',
                'nutrition_facts_ru': 'На 100 мл: Энергия 54 ккал, Белки 0,2 г, Углеводы 13 г, Жиры 0 г.',
                'nutrition_facts_uz': "100 ml ga: Energiya 54 kkal, Oqsillar 0,2 g, Uglevodlar 13 g, Yog'lar 0 g.",
                'weight_grams': 500,
                'is_featured': True,
            },
            {
                'slug': 'strawberry-preserve',
                'category': cat_preserve,
                'name': 'Strawberry Preserve',
                'name_ru': 'Клубничное варенье',
                'name_uz': "Qulupnay murabbo",
                'tagline': 'A timeless classic',
                'tagline_ru': 'Вневременная классика',
                'tagline_uz': 'Qadrdon klassika',
                'description': 'Whole strawberries slowly cooked with cane sugar to preserve their natural sweetness.',
                'description_ru': 'Цельная клубника, медленно варенная с тростниковым сахаром для сохранения естественной сладости.',
                'description_uz': "Tabiiy shirinligini saqlash uchun qamish shakari bilan sekin pishirilgan butun qulupnay.",
                'ingredients': 'Strawberries, cane sugar, lemon juice, pectin.',
                'ingredients_ru': 'Клубника, тростниковый сахар, лимонный сок, пектин.',
                'ingredients_uz': "Qulupnay, qamish shakari, limon sharbati, pektin.",
                'nutrition_facts': 'Per 100g: Energy 240kcal, Protein 0.4g, Carbohydrates 59g, Fat 0.1g.',
                'nutrition_facts_ru': 'На 100 г: Энергия 240 ккал, Белки 0,4 г, Углеводы 59 г, Жиры 0,1 г.',
                'nutrition_facts_uz': "100 g ga: Energiya 240 kkal, Oqsillar 0,4 g, Uglevodlar 59 g, Yog'lar 0,1 g.",
                'weight_grams': 350,
                'is_featured': True,
            },
            {
                'slug': 'orange-juice-1l',
                'category': cat_juice,
                'name': 'Orange Juice 1L',
                'name_ru': 'Апельсиновый сок 1л',
                'name_uz': "Apelsin sharbatlari 1l",
                'tagline': 'Sunshine in a bottle',
                'tagline_ru': 'Солнце в бутылке',
                'tagline_uz': "Shishadagi quyosh nuri",
                'description': 'Freshly squeezed Valencia oranges, not from concentrate.',
                'description_ru': 'Свежевыжатые апельсины Валенсии, не из концентрата.',
                'description_uz': "Valensiya apelsinlaridan yangi siqilgan, kontsentratsiyadan emas.",
                'ingredients': 'Orange juice.',
                'ingredients_ru': 'Апельсиновый сок.',
                'ingredients_uz': 'Apelsin sharbati.',
                'nutrition_facts': 'Per 100ml: Energy 45kcal, Protein 0.7g, Carbohydrates 10g, Fat 0.2g.',
                'nutrition_facts_ru': 'На 100 мл: Энергия 45 ккал, Белки 0,7 г, Углеводы 10 г, Жиры 0,2 г.',
                'nutrition_facts_uz': "100 ml ga: Energiya 45 kkal, Oqsillar 0,7 g, Uglevodlar 10 g, Yog'lar 0,2 g.",
                'weight_grams': 1000,
                'is_featured': False,
            },
            {
                'slug': 'apricot-nectar-500ml',
                'category': cat_nectar,
                'name': 'Apricot Nectar 0.5L',
                'name_ru': 'Абрикосовый нектар 0.5л',
                'name_uz': "O'rik nektari 0.5l",
                'tagline': 'Golden and fragrant',
                'tagline_ru': 'Золотистый и ароматный',
                'tagline_uz': "Oltin rang va hidli",
                'description': 'Ripe apricots from mountain orchards, delicately processed to retain their aroma.',
                'description_ru': 'Спелые абрикосы из горных садов, деликатно обработанные для сохранения аромата.',
                'description_uz': "Tog' bog'laridan pishgan o'rik, hidini saqlash uchun ehtiyotkorlik bilan qayta ishlangan.",
                'ingredients': 'Apricot puree, water, sugar, citric acid.',
                'ingredients_ru': 'Абрикосовое пюре, вода, сахар, лимонная кислота.',
                'ingredients_uz': "O'rik pyuresi, suv, shakar, limon kislotasi.",
                'nutrition_facts': 'Per 100ml: Energy 52kcal, Protein 0.3g, Carbohydrates 12g, Fat 0g.',
                'nutrition_facts_ru': 'На 100 мл: Энергия 52 ккал, Белки 0,3 г, Углеводы 12 г, Жиры 0 г.',
                'nutrition_facts_uz': "100 ml ga: Energiya 52 kkal, Oqsillar 0,3 g, Uglevodlar 12 g, Yog'lar 0 g.",
                'weight_grams': 500,
                'is_featured': False,
            },
            {
                'slug': 'cherry-preserve',
                'category': cat_preserve,
                'name': 'Cherry Preserve',
                'name_ru': 'Вишневое варенье',
                'name_uz': "Gilos murabbo",
                'tagline': 'Deep, bold flavor',
                'tagline_ru': 'Насыщенный, смелый вкус',
                'tagline_uz': "Boy, jasur ta'm",
                'description': 'Tart cherries balanced with just the right amount of sweetness.',
                'description_ru': 'Терпкая вишня, уравновешенная нужным количеством сладости.',
                'description_uz': "Qoniqarli shirinlik bilan muvozanatlangan nordon gilos.",
                'ingredients': 'Cherries, cane sugar, lemon juice, pectin.',
                'ingredients_ru': 'Вишня, тростниковый сахар, лимонный сок, пектин.',
                'ingredients_uz': "Gilos, qamish shakari, limon sharbati, pektin.",
                'nutrition_facts': 'Per 100g: Energy 230kcal, Protein 0.3g, Carbohydrates 57g, Fat 0.1g.',
                'nutrition_facts_ru': 'На 100 г: Энергия 230 ккал, Белки 0,3 г, Углеводы 57 г, Жиры 0,1 г.',
                'nutrition_facts_uz': "100 g ga: Energiya 230 kkal, Oqsillar 0,3 g, Uglevodlar 57 g, Yog'lar 0,1 g.",
                'weight_grams': 350,
                'is_featured': False,
            },
        ]

        for data in products_data:
            Product.objects.get_or_create(slug=data['slug'], defaults=data)

        self.stdout.write('Creating page content...')
        PageContent.objects.get_or_create(
            page_key='story',
            defaults={
                'title': 'Our Story',
                'title_ru': 'Наша история',
                'title_uz': 'Bizning hikoyamiz',
                'subtitle': 'Three decades of passion for pure fruit.',
                'subtitle_ru': 'Три десятилетия страсти к чистым фруктам.',
                'subtitle_uz': "Toza mevalarga bo'lgan ishtiyoqning uch o'n yilligi.",
                'body': (
                    '<h2>Heritage</h2><p>Founded with a simple belief: nature provides the best ingredients. '
                    'We have built our reputation on quality, transparency, and respect for the land.</p>'
                    '<h2>Values</h2><ul>'
                    '<li><strong>Quality First</strong> — Only the finest fruits make it into our products.</li>'
                    '<li><strong>Sustainability</strong> — We protect the ecosystems that nourish our ingredients.</li>'
                    '<li><strong>Community</strong> — Supporting local farmers and families for generations.</li>'
                    '</ul>'
                ),
                'body_ru': (
                    '<h2>Наследие</h2><p>Основано на простом убеждении: природа дает лучшие ингредиенты. '
                    'Мы построили свою репутацию на качестве, прозрачности и уважении к земле.</p>'
                    '<h2>Ценности</h2><ul>'
                    '<li><strong>Качество превыше всего</strong> — Только лучшие фрукты попадают в нашу продукцию.</li>'
                    '<li><strong>Устойчивость</strong> — Мы защищаем экосистемы, питающие наши ингредиенты.</li>'
                    '<li><strong>Сообщество</strong> — Поддержка местных фермеров и семей на протяжении поколений.</li>'
                    '</ul>'
                ),
                'body_uz': (
                    '<h2>Meros</h2><p>Oddiy ishonch bilan tashkil etilgan: tabiat eng yaxshi ingredientlarni beradi. '
                    'Biz o\'z obro\'mizni sifat, shaffoflik va yerga hurmat asosida qurduk.</p>'
                    '<h2>Qadriyatlar</h2><ul>'
                    '<li><strong>Avvalo sifat</strong> — Faqat eng yaxshi mevalar bizning mahsulotlarimizga tushadi.</li>'
                    '<li><strong>Barqarorlik</strong> — Biz ingredientlarimizni boqadigan ekotizimlarni himoya qilamiz.</li>'
                    '<li><strong>Jamoa</strong> — Avlodlar davomida mahalliy fermerlar va oilalarni qo\'llab-quvvatlash.</li>'
                    '</ul>'
                ),
                'meta_title': 'Our Story — Biochem',
                'meta_description': 'Discover the heritage and values behind Biochem.',
            }
        )

        PageContent.objects.get_or_create(
            page_key='sustainability',
            defaults={
                'title': 'Sustainability',
                'title_ru': 'Устойчивое развитие',
                'title_uz': 'Barqaror rivojlanish',
                'body': (
                    '<h2>Our Commitment</h2><p>We believe that producing exceptional fruit products goes hand in hand with '
                    'protecting the environment that makes them possible.</p>'
                    '<h2>Responsible Sourcing</h2><p>We work directly with local farmers who share our commitment to sustainable agriculture. '
                    'Every ingredient is traceable to its source.</p>'
                    '<h2>Reducing Our Footprint</h2><p>From energy-efficient facilities to recyclable packaging, we continuously invest in '
                    'reducing our environmental impact.</p>'
                ),
                'body_ru': (
                    '<h2>Наше обязательство</h2><p>Мы считаем, что производство исключительных фруктовых продуктов неразрывно связано с '
                    'защитой окружающей среды, которая делает их возможными.</p>'
                    '<h2>Ответственное снабжение</h2><p>Мы работаем напрямую с местными фермерами, разделяющими наше стремление к устойчивому '
                    'сельскому хозяйству. Каждый ингредиент прослеживается до его источника.</p>'
                    '<h2>Сокращение нашего следа</h2><p>От энергоэффективных объектов до перерабатываемой упаковки — мы постоянно инвестируем в '
                    'сокращение нашего воздействия на окружающую среду.</p>'
                ),
                'body_uz': (
                    '<h2>Bizning majburiyatimiz</h2><p>Biz ajoyib meva mahsulotlarini ishlab chiqarish ularni mumkin qiluvchi atrof-muhitni '
                    'himoya qilish bilan uzviy bog\'liq deb hisoblaymiz.</p>'
                    '<h2>Mas\'uliyatli ta\'minot</h2><p>Biz barqaror qishloq xo\'jaligiga bo\'lgan intilishimizni baham ko\'radigan mahalliy '
                    'fermerlar bilan bevosita ishlaymiz. Har bir ingredient o\'z manbasiga qadar kuzatib boriladi.</p>'
                    '<h2>Ortiqcha izni kamaytirish</h2><p>Energiya samarali obyektlardan qayta ishlanadigan qadoqlashgacha, biz doimiy ravishda '
                    'atrof-muhitga ta\'sirni kamaytirishga sarmoya kiritamiz.</p>'
                ),
                'meta_title': 'Sustainability — Biochem',
                'meta_description': 'Learn about our commitment to sustainable fruit production.',
            }
        )

        self.stdout.write('Creating content blocks...')
        ContentBlock.objects.get_or_create(
            block_key='home_story',
            defaults={
                'title': 'Our Story',
                'title_ru': 'Наша история',
                'title_uz': 'Bizning hikoyamiz',
                'body': 'For over three decades, we have been cultivating the finest fruits and transforming them into premium products that bring nature to your table.',
                'body_ru': 'На протяжении более трех десятилетий мы выращиваем лучшие фрукты и превращаем их в премиальную продукцию.',
                'body_uz': "Uch o'n yildan ortiq vaqt davomida biz eng yaxshi mevalarni yetishtiramiz va ularni yuqori sifatli mahsulotlarga aylantiramiz.",
                'order': 1,
            }
        )
        ContentBlock.objects.get_or_create(
            block_key='home_hero',
            defaults={
                'title': 'Welcome',
                'order': 0,
            }
        )
        ContentBlock.objects.get_or_create(
            block_key='home_featured',
            defaults={
                'title': 'Featured Products',
                'title_ru': 'Избранные продукты',
                'title_uz': 'Tavsiya etilgan mahsulotlar',
                'order': 2,
            }
        )

        self.stdout.write('Creating hero slides...')
        slides_data = [
            {
                'headline': 'PURE NATURE IN EVERY DROP',
                'headline_ru': 'ЧИСТАЯ ПРИРОДА В КАЖДОЙ КАПЛЕ',
                'headline_uz': "HAR TOMCHIDA TOZA TABIIYAT",
                'subheadline': 'Premium fruit products crafted with care.',
                'subheadline_ru': 'Премиальная фруктовая продукция, созданная с заботой.',
                'subheadline_uz': "G'amxo'rlik bilan yaratilgan yuqori sifatli meva mahsulotlari.",
                'cta_text': 'Explore Products',
                'cta_text_ru': 'Смотреть продукцию',
                'cta_text_uz': 'Mahsulotlarni ko\'rish',
                'cta_url': '/en/products/',
                'order': 1,
            },
            {
                'headline': 'HERITAGE MEETS QUALITY',
                'headline_ru': 'НАСЛЕДИЕ ВСТРЕЧАЕТ КАЧЕСТВО',
                'headline_uz': 'MEROS SIFAT UCHRASHADI',
                'subheadline': 'Three decades of passion for pure fruit.',
                'subheadline_ru': 'Три десятилетия страсти к чистым фруктам.',
                'subheadline_uz': "Toza mevalarga bo'lgan ishtiyoqning uch o'n yilligi.",
                'cta_text': 'Our Story',
                'cta_text_ru': 'Наша история',
                'cta_text_uz': 'Bizning hikoyamiz',
                'cta_url': '/en/story/',
                'order': 2,
            },
            {
                'headline': 'SUSTAINABLE BY DESIGN',
                'headline_ru': 'УСТОЙЧИВОСТЬ ПО ЗАДУМКЕ',
                'headline_uz': "DIZYN BO'YICHA BARQAROR",
                'subheadline': 'Protecting the land that feeds us.',
                'subheadline_ru': 'Защищаем землю, которая нас кормит.',
                'subheadline_uz': "Bizni boqadigan yerni himoya qilamiz.",
                'cta_text': 'Learn More',
                'cta_text_ru': 'Узнать больше',
                'cta_text_uz': "Ko'proq o'qish",
                'cta_url': '/en/sustainability/',
                'order': 3,
            },
        ]
        for data in slides_data:
            HeroSlide.objects.get_or_create(
                headline=data['headline'],
                defaults=data,
            )

        self.stdout.write(self.style.SUCCESS('Bootstrap complete!'))
