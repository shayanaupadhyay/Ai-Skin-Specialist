---
name: Clinical Intelligence Interface
colors:
  surface: '#f9f9ff'
  surface-dim: '#cbdaff'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f3ff'
  surface-container: '#e9edff'
  surface-container-high: '#e0e8ff'
  surface-container-highest: '#d8e2ff'
  on-surface: '#081b3a'
  on-surface-variant: '#434655'
  inverse-surface: '#1f3050'
  inverse-on-surface: '#edf0ff'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#006a61'
  on-secondary: '#ffffff'
  secondary-container: '#86f2e4'
  on-secondary-container: '#006f66'
  tertiary: '#943700'
  on-tertiary: '#ffffff'
  tertiary-container: '#bc4800'
  on-tertiary-container: '#ffede6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#89f5e7'
  secondary-fixed-dim: '#6bd8cb'
  on-secondary-fixed: '#00201d'
  on-secondary-fixed-variant: '#005049'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb596'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#7d2d00'
  background: '#f9f9ff'
  on-background: '#081b3a'
  surface-variant: '#d8e2ff'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style

The design system is engineered for high-stakes medical AI environments where clarity, precision, and a sense of "digital calm" are paramount. The target audience includes healthcare professionals and patients who require a trustworthy, clinical, and sophisticated experience. 

The visual style is **Modern Corporate** with a heavy emphasis on **Tonal Minimalism**. It utilizes generous whitespace to reduce cognitive load and large-scale rounded containers to soften the technical nature of AI interactions. By combining high-legibility typography with a structured modular layout, the system evokes an emotional response of security, professional reliability, and technological advancement without appearing overly experimental or "start-up" playful.

## Colors

The palette is rooted in "Clinical Blue" and "Pure White" to establish an immediate association with healthcare hygiene and professional technology. 

- **Primary Accent (#2563EB):** Used for critical actions, active states, and primary medical data highlights.
- **Success/Secondary (#0D9488):** Reserved for positive health outcomes, verified statuses, and stability indicators.
- **Neutral/Text (#1A2B4B):** A deep navy used for maximum legibility in body text and headings, providing better contrast than pure black.
- **Surface (#F0F7FF):** A pale tint used for card backgrounds and subtle section nesting to differentiate between global navigation and specific data modules.

## Typography

The design system utilizes **Inter** for its exceptional legibility and systematic performance in data-heavy interfaces. 

- **Weight Usage:** Use `SemiBold` (600) for all semantic headings to create a clear hierarchy against medical charts and data.
- **Reading Comfort:** Body text should maintain a 1.5x line-height ratio to ensure patient reports and AI transcriptions remain readable during long sessions.
- **Micro-copy:** Use the `label-md` style for category tags (e.g., "DIAGNOSIS", "PATIENT INFO") to create a structured, tabular feel without the need for heavy borders.

## Layout & Spacing

This design system employs a **Modular Grid** philosophy tailored for Gradio-style dashboard blocks. 

- **Structure:** Content is organized into independent cards that sit on a 12-column grid for desktop.
- **Margins:** Large 48px outer margins on desktop enforce a premium, spacious feel. On mobile, this reduces to 16px to maximize data visualization real estate.
- **Rhythm:** An 8px base unit governs all padding. Standard card internal padding is `md` (24px) to ensure content doesn't feel cramped against the rounded edges.
- **Reflow:** For tablet and mobile, modules stack vertically. Complex medical tables should switch to a card-list format or allow horizontal overflow with a persistent "Action" column.

## Elevation & Depth

Visual hierarchy is achieved through a combination of **Tonal Layering** and **Ambient Shadows**.

- **Surfaces:** The primary background is white (#FFFFFF). Elevated modules and dashboard cards use a Very Pale Blue (#F0F7FF) surface.
- **Shadows:** Shadows are intentionally soft and diffused to maintain a friendly clinical atmosphere. Use a dual-layered shadow for primary cards: `0px 4px 20px rgba(26, 43, 75, 0.05)` and `0px 10px 40px rgba(26, 43, 75, 0.03)`. 
- **Z-Index:** Navigation sidebars sit at the highest elevation when on mobile (drawers), while desktop modules remain flat with subtle 1px inner borders (`#E2E8F0`) to define edges without adding visual weight.

## Shapes

The shape language is defined by large, welcoming radii. 

- **Cards/Modules:** Use `rounded-xl` (1.5rem / 24px) for all main dashboard containers to create the "premium medical" aesthetic.
- **Interactive Elements:** Buttons and input fields use `rounded-lg` (1rem / 16px) to match the container language while maintaining distinct clickability.
- **Status Pills:** Icons and small status indicators should use full pill-shaping (9999px) to differentiate them from functional UI blocks.

## Components

- **Primary Buttons:** High-contrast Clinical Blue (#2563EB) backgrounds with white text. Use 16px rounded corners. Transitions should be a subtle color shift rather than a physical movement.
- **Medical Cards:** Utilize the `surface_color` with a 24px corner radius. Include a 1px border (#E2E8F0) to ensure high-contrast accessibility.
- **Input Fields:** Pure white background with a soft slate (#64748B) border. On focus, the border transitions to Clinical Blue with a 3px soft outer glow.
- **Iconography:** Use 2px stroke weight icons. Key symbols (Shield for security, Waveform for AI/Vitals, Stethoscope for clinical) should be encased in a soft teal (#0D9488) circular background at 10% opacity.
- **Progress Indicators:** Use the soft teal for "Active AI Analysis" states to keep the user calm during processing times.
- **Checkboxes/Radios:** Use the same 16px rounding logic—radios are standard circles, but checkboxes should have a generous 4px radius for a softer medical feel.