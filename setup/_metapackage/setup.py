import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-l10n-taiwan",
    description="Meta package for oca-l10n-taiwan Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-l10n_taiwan',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
