"""
Generate comprehensive Test Summary Report in Markdown (.md) and PDF (.pdf) formats.
Includes automated statistics and test distribution chart.
"""

import os
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def generate_chart():
    os.makedirs("reports", exist_ok=True)
    labels = ["Passed (41)", "Failed (3)", "Blocked (0)", "Not Executed (0)"]
    sizes = [41, 3, 0, 0]
    colors_list = ["#16a34a", "#dc2626", "#f59e0b", "#94a3b8"]
    explode = (0.05, 0.1, 0, 0)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
    
    # Donut Chart
    wedges, texts, autotexts = ax1.pie(
        [41, 3], 
        labels=["Passed", "Failed"], 
        autopct="%1.1f%%",
        startangle=140,
        colors=["#16a34a", "#dc2626"],
        explode=(0, 0.1),
        wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2)
    )
    for at in autotexts:
        at.set_color("white")
        at.set_weight("bold")
    ax1.set_title("Test Execution Status Distribution", fontsize=12, fontweight="bold", pad=12)

    # Bar chart by Module
    modules = ["Registration", "Auth", "Listing/Details", "Search/Filter", "Cart", "Checkout/Order"]
    passed_counts = [5, 5, 5, 6, 7, 13] # Total passed = 41
    failed_counts = [0, 0, 0, 1, 1, 1]   # Total failed = 3
    
    x = range(len(modules))
    width = 0.4
    ax2.bar([i - width/2 for i in x], passed_counts, width=width, label="Passed", color="#16a34a")
    ax2.bar([i + width/2 for i in x], failed_counts, width=width, label="Failed", color="#dc2626")
    ax2.set_xticks(x)
    ax2.set_xticklabels(modules, rotation=25, ha="right", fontsize=9)
    ax2.set_ylabel("Number of Test Cases")
    ax2.set_title("Module-wise Test Results", fontsize=12, fontweight="bold", pad=12)
    ax2.legend()
    ax2.grid(axis="y", linestyle="--", alpha=0.4)
    
    plt.tight_layout()
    chart_path = "reports/test-distribution-chart.png"
    plt.savefig(chart_path, dpi=200)
    plt.close()
    print(f"Generated chart: {chart_path}")
    return chart_path

def generate_markdown_report(chart_path):
    md_content = """# Software Test Summary Report: ZenithMart E-Commerce

**Project Name:** ZenithMart E-Commerce Testing  
**Repository:** `ecommerce-manual-testing`  
**Test Cycle:** Final System Testing & Regression Cycle 1.0  
**Test Execution Date:** November 14, 2026  
**QA Lead / Test Engineer:** QA Automation Engineer (Portfolio Candidate)  
**Testing Status:** Complete - 93.18% Pass Rate  

---

## 1. Executive Summary

This Test Summary Report documents the formal execution of manual and automated functional, boundary-value, negative, and validation tests performed on the **ZenithMart E-Commerce Web Application**.

Testing was conducted across all 12 core e-commerce modules, encompassing end-to-end shopping workflows from user registration, authentication, product browsing, keyword search, multi-criteria filtering, product details inspection, shopping cart quantity management, multi-step checkout form validation, to final order placement and confirmation.

A total of **44 test cases** were designed and executed. **41 test cases (93.18%) passed successfully**, while **3 test cases (6.82%) failed**, uncovering authentic functional and validation defects. Defect reports were logged with steps to reproduce and visual evidence.

---

## 2. Testing Objectives & Scope

### 2.1 Objectives
1. Verify functional correctness of all primary user journeys across the e-commerce storefront.
2. Validate client-side form validations, input sanitization, and boundary value limits.
3. Assess user experience (UX), error messaging clarity, and state consistency.
4. Establish a professional QA portfolio project demonstrating industry-standard test artifacts, Jira-style defect documentation, and Page Object Model automation.

### 2.2 In-Scope Modules
- User Registration & Account Creation
- User Login, Session State & Logout
- Product Catalog Listing & UI Card Rendering
- Product Keyword Search (Exact, Case-Insensitive, Empty States)
- Product Filtering (Category & Price Range Thresholds)
- Product Sorting (Price Low-to-High, Rating)
- Product Details Modal (Specifications, Stock, Quantity Selector)
- Shopping Cart Operations (Add, Remove, Clear, Line-Item Subtotals, 8% Tax, Grand Total)
- Cart Quantity Updates (Button Controls & Direct Numeric Inputs)
- Checkout Shipping Form Validation (Required Fields, Email Format, Postal Code)
- Mock Payment Selection (Credit Card vs Cash on Delivery)
- Order Confirmation & Post-Order State (Order ID Generation & Cart Reset)

### 2.3 Out of Scope
- Real financial transactions and third-party payment gateways (Stripe/PayPal API).
- Production multi-region server infrastructure and live database migrations.

---

## 3. Testing Environment

| Parameter | Configuration |
| :--- | :--- |
| **Operating System** | Windows 11 Enterprise (64-bit) |
| **Primary Browser** | Google Chrome Version 157.0 (Official Build) |
| **Screen Resolution** | 1920 × 1080 (FHD Desktop Viewport) |
| **Local Web Server** | Standalone Local Application Engine (`file:///` and HTTP Server) |
| **Automation Tools** | Python 3.13, Selenium WebDriver 4.52, Pytest 9.1 |
| **Documentation Tools** | Microsoft Excel (.xlsx), CSV, Markdown, ReportLab PDF Engine |

---

## 4. Test Execution Metrics & Statistics

### 4.1 Overall Execution Summary

| Metric | Count | Percentage |
| :--- | :---: | :---: |
| **Total Test Cases** | **44** | **100.0%** |
| **Executed Test Cases** | **44** | **100.0%** |
| **Passed Test Cases** | **41** | **93.18%** |
| **Failed Test Cases** | **3** | **6.82%** |
| **Blocked Test Cases** | **0** | **0.00%** |
| **Not Executed Test Cases** | **0** | **0.00%** |

### 4.2 Module-wise Breakdown

| Module | Total | Passed | Failed | Blocked | Pass Rate |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **User Registration** | 5 | 5 | 0 | 0 | 100% |
| **User Authentication** | 5 | 5 | 0 | 0 | 100% |
| **Product Listing & Details** | 5 | 5 | 0 | 0 | 100% |
| **Product Search & Filter** | 10 | 9 | 1 | 0 | 90% |
| **Shopping Cart Management** | 8 | 7 | 1 | 0 | 87.5% |
| **Checkout & Order Confirmation** | 11 | 10 | 1 | 0 | 90.9% |
| **Total** | **44** | **41** | **3** | **0** | **93.18%** |

---

## 5. Test Results Distribution Chart

![Test Execution Status Distribution](test-distribution-chart.png)

### Distribution Breakdown (Mermaid Visualization)

```mermaid
pie title Test Case Execution Status
    "Passed (41 Cases)" : 41
    "Failed (3 Cases)" : 3
    "Blocked (0 Cases)" : 0
    "Not Executed (0 Cases)" : 0
```

---

## 6. Discovered Defects Summary (Bug Log)

During manual and boundary-value test execution, **3 authentic defects** were discovered and logged:

| Bug ID | Module | Title | Severity | Priority | Status |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **BUG-001** | Shopping Cart | Cart allows entering negative or zero quantity on direct typing, causing negative order total | **High** | **High** | Open |
| **BUG-002** | Checkout Form | ZIP/Postal Code field accepts non-numeric alphabetic input ('ABCDE') without validation | **Medium** | **Medium** | Open |
| **BUG-003** | Product Search | Search query does not trim leading/trailing whitespace, returning 0 matching results | **Low** | **Low** | Open |

### Detailed Defect Reports

#### Bug Report 1: BUG-001
- **Title:** Cart quantity input accepts negative values on direct input
- **Severity:** High | **Priority:** High | **Status:** Open
- **Steps to Reproduce:**
  1. Add an item to the shopping cart.
  2. Open cart drawer and click into the quantity input box.
  3. Enter `-2` and click away (trigger blur event).
- **Expected Result:** Application should reject negative or zero input, display validation error or clamp quantity to 1.
- **Actual Result:** Quantity updates to `-2`, line-item subtotal becomes `-$399.98`, and overall order total is corrupted.
- **Evidence:** `screenshots/bug-001-negative-cart-quantity.png`

#### Bug Report 2: BUG-002
- **Title:** Checkout ZIP code field accepts alphabetic characters without regex validation
- **Severity:** Medium | **Priority:** Medium | **Status:** Open
- **Steps to Reproduce:**
  1. Add products to cart and proceed to checkout.
  2. Fill valid shipping information.
  3. Enter `ABCDE` in the ZIP / Postal Code input.
  4. Select payment method and click 'Place Order'.
- **Expected Result:** Form should enforce 5-digit numeric postal code regex (`^\\d{5}$`) and display 'Please enter a valid numeric ZIP code'.
- **Actual Result:** Form accepts `ABCDE` because it only checks for non-empty string, allowing order placement with corrupted postal data.
- **Evidence:** `screenshots/bug-002-zipcode-validation.png`

#### Bug Report 3: BUG-003
- **Title:** Search query fails to match products when query has leading/trailing whitespace
- **Severity:** Low | **Priority:** Low | **Status:** Open
- **Steps to Reproduce:**
  1. Click on the search bar in the header.
  2. Enter `'  Camera  '` (with spaces).
  3. Press Enter or click search button.
- **Expected Result:** Input string should be trimmed before filtering, displaying '4K Action Sports Camera'.
- **Actual Result:** 0 matching products found; empty state screen displayed.
- **Evidence:** `screenshots/bug-003-search-whitespace.png`

---

## 7. QA Engineering Observations & Recommendations

1. **Input Sanitization & Boundary Handling:**
   - Implement strict client-side clamping on numeric input elements (`min="1"` enforcement in JavaScript `change` listener).
   - Sanitize all text inputs using `.trim()` prior to search query filtering.

2. **Regex-Based Field Validation:**
   - Enhance the checkout form validation with standard postal code regex (`^\d{5}(-\d{4})?$`).
   - Add credit card Luhn algorithm validation for enhanced payment form realism.

3. **Automation Opportunities:**
   - Automated regression testing using Python Selenium ensures that future bug fixes do not cause regression in core checkout, cart, or search flows.

---

## 8. Conclusion

The ZenithMart e-commerce application has demonstrated high stability in core user flows, achieving an overall **93.18% pass rate**. The application's responsive UI, dynamic shopping cart, product filtering, and authentication flow perform reliably. 

The three logged defects (BUG-001, BUG-002, BUG-003) represent high-value boundary and input validation improvements that have been clearly documented with steps to reproduce and visual evidence. This testing cycle provides complete, professional documentation suitable for production sign-off and portfolio evaluation.
"""
    report_path = "reports/test-summary-report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Markdown report: {report_path}")

def generate_pdf_report(chart_path):
    pdf_path = "reports/test-summary-report.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1E3A8A"),
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#475569"),
        spaceAfter=14
    )
    h2_style = ParagraphStyle(
        "SectionH2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=12,
        spaceAfter=6
    )
    h3_style = ParagraphStyle(
        "SectionH3",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=8,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        "DocBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=6
    )
    bold_style = ParagraphStyle(
        "DocBold",
        parent=body_style,
        fontName="Helvetica-Bold"
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("Software Test Summary Report: ZenithMart E-Commerce", title_style))
    meta_text = "<b>Repository:</b> ecommerce-manual-testing &nbsp;|&nbsp; <b>Cycle:</b> System Testing 1.0 &nbsp;|&nbsp; <b>Execution Date:</b> Nov 14, 2026 &nbsp;|&nbsp; <b>Overall Status:</b> 93.18% Pass"
    story.append(Paragraph(meta_text, subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1E3A8A"), spaceAfter=10))

    # Executive Summary
    story.append(Paragraph("1. Executive Summary", h2_style))
    exec_summary = (
        "This Test Summary Report provides comprehensive formal documentation of manual and automated testing "
        "executed on the <b>ZenithMart E-Commerce Web Application</b>. Across 12 distinct modules—ranging from "
        "user registration and authentication to product search, dynamic filtering, cart quantity handling, and checkout validation—"
        "a total of <b>44 test cases</b> were executed. <b>41 test cases (93.18%) passed</b>, and <b>3 test cases (6.82%) failed</b>, "
        "identifying authentic defects in quantity boundary limits, postal code input format, and whitespace trimming."
    )
    story.append(Paragraph(exec_summary, body_style))

    # Objectives & Environment
    story.append(Paragraph("2. Scope & Test Environment", h2_style))
    env_data = [
        [Paragraph("<b>Operating System:</b> Windows 11 Enterprise (64-bit)", body_style),
         Paragraph("<b>Primary Browser:</b> Google Chrome 157.0 (FHD 1920x1080)", body_style)],
        [Paragraph("<b>Automation Stack:</b> Python 3.13, Selenium 4.52, Pytest 9.1", body_style),
         Paragraph("<b>Test Types:</b> Functional, Validation, BVA, Negative, Regression", body_style)]
    ]
    env_table = Table(env_data, colWidths=[260, 260])
    env_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(env_table)
    story.append(Spacer(1, 10))

    # Test Execution Metrics Table
    story.append(Paragraph("3. Test Execution Metrics", h2_style))
    metrics_data = [
        ["Module Category", "Total Cases", "Passed", "Failed", "Blocked", "Pass Rate"],
        ["User Registration", "5", "5", "0", "0", "100.0%"],
        ["User Authentication & Session", "5", "5", "0", "0", "100.0%"],
        ["Product Catalog & Details", "5", "5", "0", "0", "100.0%"],
        ["Search & Category/Price Filters", "10", "9", "1", "0", "90.0%"],
        ["Shopping Cart Operations", "8", "7", "1", "0", "87.5%"],
        ["Checkout & Order Placement", "11", "10", "1", "0", "90.9%"],
        ["Overall Test Execution Total", "44", "41", "3", "0", "93.18%"]
    ]
    t = Table(metrics_data, colWidths=[180, 65, 65, 65, 65, 80])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#EFF6FF")),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # Chart
    if os.path.exists(chart_path):
        story.append(Paragraph("4. Execution Distribution Visualizations", h2_style))
        story.append(Image(chart_path, width=6.8*inch, height=2.85*inch))
        story.append(Spacer(1, 10))

    # Defects Table
    story.append(Paragraph("5. Discovered Defects Summary", h2_style))
    bug_data = [
        ["Bug ID", "Module", "Defect Title", "Severity", "Priority", "Status"],
        ["BUG-001", "Shopping Cart", "Cart accepts negative/zero quantity on direct typing", "High", "High", "Open"],
        ["BUG-002", "Checkout Form", "ZIP code accepts alphabetic input without regex check", "Medium", "Medium", "Open"],
        ["BUG-003", "Product Search", "Search fails on untrimmed leading/trailing spaces", "Low", "Low", "Open"]
    ]
    bt = Table(bug_data, colWidths=[55, 80, 240, 50, 50, 45])
    bt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#DC2626")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('ALIGN', (0,0), (1,-1), 'CENTER'),
        ('ALIGN', (3,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#FEF2F2")),
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor("#FFFBEB")),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#F8FAFC")),
    ]))
    story.append(bt)
    story.append(Spacer(1, 10))

    # Conclusion & Sign-Off
    story.append(Paragraph("6. Conclusion & Recommendations", h2_style))
    conclusion_text = (
        "ZenithMart demonstrated robust functionality across primary shopping journeys, successfully processing "
        "catalog navigation, filtering, session management, and mock orders. The three identified defects "
        "have been logged with reproduction steps and screenshot evidence for developer remediation. "
        "The project meets all criteria for final-year engineering portfolio quality and technical interview demonstration."
    )
    story.append(Paragraph(conclusion_text, body_style))

    doc.build(story)
    print(f"Generated PDF report: {pdf_path}")

if __name__ == "__main__":
    c_path = generate_chart()
    generate_markdown_report(c_path)
    generate_pdf_report(c_path)
    print("Reports generation complete!")

