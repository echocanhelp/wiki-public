# Taiwanese American Historical Society — Website Content Specification

> **Domain**: tah-society.org
> **Purpose**: Non-profit verification landing page + informational sub-pages
> **Build target**: Markdown → HTML (pandoc or Python markdown)
> **Color theme**: Deep navy (#0A1929) + gold accent (#D4AF37)
> **Typography**: Noto Serif (body) + Noto Sans (headings)

---

## Site Structure

```
tah-society.org/
├── /                  (Landing page)
├── /contact           (Contact Us)
├── /mission           (Our Mission)
├── /board             (Board Members)
└── /echopedia         (Link to Echopedia knowledge hub)
```

---

## Page 1: Landing Page (/)

### Header
- **Logo**: TAHS seal (placeholder SVG)
- **Nav**: Home | Contact | Mission | Board | Echopedia

### Hero Section
**Title**: Taiwanese American Historical Society

**Subtitle**: Preserving, documenting, and promoting Taiwanese American history and culture

**Call-to-action buttons**:
- [Donate Now] → /contact (anchor: donate)
- [Learn More] → /mission

### Legal Identity Block
**Organizational Status**: 501(c)(3) Non-Profit Public Charity

| Field | Value |
|-----|-------|
| **Legal name** | Taiwanese American Historical Society |
| **Chinese name** | 台美人歷史協會 |
| **Short name** | TAHS |
| **EIN** | 46-4005384 |
| **Federal tax status** | IRC §501(c)(3) public charity |
| **Public charity status** | 170(b)(1)(A)(vi) |
| **Contribution deductibility** | Yes (IRC §170) |
| **Effective date of exemption** | June 18, 2024 |
| **IRS determination letter date** | June 27, 2024 |
| **Accounting period** | December 31 |
| **DLN** | 26053572010194 |

### Mission Statement
The Taiwanese American Historical Society (TAHS) is dedicated to documenting, preserving, and promoting Taiwanese American history, culture, and heritage. We work to build community connections across generations, support research and education about Taiwanese American experiences, and maintain digital archives and knowledge bases.

### Key Activities
1. **Exhibitions** — Historical materials exhibitions (228 Historical Materials, pre-WWII Formosan students in US, Taiwan puppet theater)
2. **Book Launches** — Introducing works by Taiwanese American authors
3. **Political Engagement** — Supporting pro-Taiwan grassroots diplomacy (501(c)(3) compliant)
4. **Profile Interviews** — Recording oral histories of Taiwanese American leaders
5. **Memorial Services** — Honoring deceased community members
6. **Historical Symposia** — Regular historical review and prospect symposia
7. **Special Lectures** — Talks on Taiwan history, culture, and art
8. **Intergenerational Gatherings** — Connecting first-generation and younger-generation Taiwanese Americans
9. **Historical Material Collection** — Digitization and preservation of historical materials

### Founding Information
- **Founded**: December 11, 2013
- **Founding location**: Hilton Hotel, San Gabriel, CA
- **Founding conference**: Press conference held at founding
- **Founding essay**: 周威霖 (Zhou Weilin), "緣起與展望" (Origins and Prospects)

### Founders
| Name | Role |
|------|------|
| 鄭炳全 (Zheng Bingquan) | First convener |
| 楊嘉猷 (Charles Yang) | Founding president |
| 周威霖 (Zhou Weilin) | Secretary |
| 王耀廷 (Wang Yao-ting) | Vice president |

### Presidents
| Name | Term |
|------|------|
| 楊嘉猷 (Charles Yang) | Founding president |
| Franklin Ping Cheng | 2014–2017 |
| 許景鴻 (Leonard Hsu Jr.) | Current (on record) |

### Contact Information
**Mailing address**:
```
Taiwanese American Historical Society
c/o Leonard Hsu
279 S. Main St
Orange, CA 92868
```

**Email**: info@tahs-society.org

**Phone**: (TBD)

### Quick Links
- [Echopedia — Community Knowledge Hub](/echopedia)
- [YouTube Channel](https://youtube.com/@TAhistory)
- [Existing Site](http://www.TAhistory.org)

### Footer
```
© 2024 Taiwanese American Historical Society
EIN: 46-4005384 | 501(c)(3) Public Charity
tah-society.org
```

---

## Page 2: Contact Us (/contact)

### Contact Information

**Mailing Address**:
```
Taiwanese American Historical Society
c/o Leonard Hsu
279 S. Main St
Orange, CA 92868
USA
```

**Email**: info@tahs-society.org

**Phone**: (TBD)

**IRS Determination Letter**: Available upon request. Please contact us with your organization's verification requirements.

### Contact Form
- Name
- Email
- Subject
- Message

### Office Hours
By appointment only.

### Social Media
- YouTube: @TAhistory
- Facebook: Taiwanese American Historical Society
- (Other platforms TBD)

### Schema.org Markup
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Taiwanese American Historical Society",
  "alternateName": "TAHS",
  "legalName": "Taiwanese American Historical Society",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "279 S. Main St",
    "addressLocality": "Orange",
    "addressRegion": "CA",
    "postalCode": "92868",
    "addressCountry": "US"
  },
  "taxID": "46-4005384",
  "url": "https://tah-society.org",
  "sameAs": [
    "https://youtube.com/@TAhistory",
    "http://www.TAhistory.org"
  ]
}
```

---

## Page 3: Our Mission (/mission)

### Our Mission
The Taiwanese American Historical Society (TAHS) is a 501(c)(3) non-profit organization dedicated to documenting, preserving, and promoting Taiwanese American history, culture, and heritage.

### Our Vision
A future where Taiwanese American stories are preserved, accessible, and recognized as an integral part of the American narrative.

### Our Core Values
1. **歷史傳承 (Historical Inheritance)** — Preserving the past for future generations
2. **族群榮譽 (Ethnic Honor)** — Honoring our community's contributions
3. **全民團結 (People's Unity)** — Building bridges across communities
4. **社會責任 (Social Responsibility)** — Giving back to society
5. **前途希望 (Future Hope)** — Investing in the next generation

### Charitable Purpose (IRC §501(c)(3))
TAHS operates exclusively for charitable, educational, and scientific purposes within the meaning of IRC §501(c)(3). Specifically, we:

1. **Document** Taiwanese American historical records and oral histories
2. **Preserve** historical materials through digitization and archival storage
3. **Promote** Taiwanese American history through exhibitions, lectures, and publications
4. **Educate** the public about Taiwanese American experiences and contributions
5. **Build community** connections across generations of Taiwanese Americans

### Activities
See "Key Activities" section on the landing page for full list.

### No Private Benefit
TAHS does not operate for the benefit of private shareholders or individuals. No part of the net earnings of the organization inures to the benefit of any private shareholder or individual.

### No Political Campaign Activity
TAHS does not participate in or intervene in any political campaign on behalf of or in opposition to any candidate for public office.

---

## Page 4: Board Members (/board)

### Current Board

**許景鴻 (Leonard Hsu Jr.)** — President
- Role: President, Taiwanese American Historical Society
- Background: Community leader, technical architect
- Contact: c/o Leonard Hsu, 279 S. Main St, Orange, CA 92868

**Franklin Ping Cheng** — Former President (2014–2017)
- Role: Past President
- Background: Led TAHS through 2014–2017 term

**楊嘉猷 (Charles Yang)** — Founding President
- Role: Founding President
- Background: Author of founding essay "緣起與展望"

### Board of Directors (Historical)
| Name | Role | Term |
|------|------|------|
| 楊嘉猷 (Charles Yang) | Founding President | 2013 |
| Franklin Ping Cheng | President | 2014–2017 |
| 許景鴻 (Leonard Hsu Jr.) | President | 2024–present |
| 周威霖 (Zhou Weilin) | Secretary | 2013–present |
| 王耀廷 (Wang Yao-ting) | Vice President | 2013–present |
| 鄭炳全 (Zheng Bingquan) | First Convener | 2013 |

### Board Meeting Schedule
Board meetings are held regularly. Contact us for the current schedule.

### Board Member Bios
- **Leonard Hsu Jr. (許景鴻)**: Current president of TAHS. Community leader focused on digital preservation of Taiwanese American history. Manages the Echopedia knowledge hub.
- **Franklin Ping Cheng**: Served as president from 2014 to 2017. Led the organization through its early development years.
- **Charles Yang (楊嘉猷)**: Founding president. Authored the foundational essay "緣起與展望" that established TAHS's ideological foundation.

---

## Page 5: Echopedia (/echopedia)

### Link to Echopedia
The Taiwanese American Historical Society maintains Echopedia, a living digital archive of Taiwanese American history and culture.

**Visit Echopedia**: [echopedia.tahs-society.org](https://echopedia.tahs-society.org)

### What is Echopedia?
Echopedia is the evolution of TAHS's publication method. Where the yearbooks (2017, 2023) captured a moment in time, Echopedia is the continuously evolving memory of the Taiwanese American community.

### Features
- Full-text search across all entries
- Hyperlinked graph of people, organizations, and events
- Multimedia support (photos, audio, video, documents)
- Community contributions welcome

---

## Design Specifications

### Color Palette
| Use | Color |
|-----|-------|
| Primary (navy) | #0A1929 |
| Accent (gold) | #D4AF37 |
| Background | #FFFFFF |
| Text | #333333 |
| Light text | #666666 |
| Border | #E0E0E0 |

### Typography
- **Body**: Noto Serif, Georgia, serif
- **Headings**: Noto Sans, Arial, sans-serif
- **Chinese**: Noto Serif TC, PMingLiU, serif

### Layout
- Max width: 800px
- Padding: 24px (mobile: 16px)
- Line height: 1.6
- Mobile-first responsive

### CSS Classes
```
.container    — max-width wrapper
.header       — site header
.nav          — navigation bar
.hero         — hero section
.content      — main content
.footer       — site footer
.btn          — button
.btn-primary    — gold button
.btn-secondary  — navy button
.table        — styled table
.address      — formatted address block
```

### Schema.org Structured Data
Each page should include JSON-LD structured data:
- Landing page: `Organization` schema
- Contact page: `Organization` + `PostalAddress` schema
- Mission page: `Organization` schema with `foundingDate`
- Board page: `Organization` schema with `member` array

### SEO Metadata
Each page should include:
- `<title>`: Page title + " | Taiwanese American Historical Society"
- `<meta name="description">`: 150-160 char description
- `<meta name="viewport">`: responsive
- `<link rel="canonical">`: canonical URL

---

## Build Instructions

### Prerequisites
- Python 3.x (for markdown conversion)
- OR pandoc (preferred)

### Build Script
```bash
#!/bin/bash
# build.sh — Convert markdown to HTML

set -e

SITE_DIR="$(dirname "$0")"
DIST_DIR="$SITE_DIR/dist"
mkdir -p "$DIST_DIR"

# Copy assets
cp "$SITE_DIR/style.css" "$DIST_DIR/"
cp -r "$SITE_DIR/assets" "$DIST_DIR/" 2>/dev/null || true

# Convert each markdown file to HTML
for md in "$SITE_DIR"/*.md; do
    [ "$(basename "$md")" = "TAHS_WEBSITE.md" ] && continue  # Skip this spec file
    html="$DIST_DIR/$(basename "${md%.md}").html"
    python3 -c "
import markdown
with open('$md') as f:
    text = f.read()
html_content = markdown.markdown(text, extensions=['tables', 'fenced_code'])
print(html_content)
" > "$html"
done

echo "Build complete. Output in $DIST_DIR/"
```

### Deployment
1. Upload `dist/` contents to tah-society.org root
2. Configure DNS for tah-society.org
3. Set up HTTPS (Let's Encrypt)
4. Configure redirects from www.TAhistory.org

---

## Verification Platform Requirements Checklist

### GuideStar / Charity Navigator
- [x] Legal name and EIN
- [x] 501(c)(3) status and effective date
- [x] Physical address
- [x] Mission statement
- [x] Contact information
- [x] Board member listing

### Donation Processors (Network for Good, etc.)
- [x] 501(c)(3) status
- [x] EIN
- [x] Contact page with email
- [x] Mission statement
- [x] Physical address for verification

### ProPublica Nonprofit Explorer
- [x] EIN (already in IRS database)
- [x] Legal name
- [ ] Form 990 (not required on website, available from IRS)

### Google for Nonprofits
- [x] 501(c)(3) status
- [x] EIN
- [x] Physical address
- [x] Contact information
- [x] Mission statement
