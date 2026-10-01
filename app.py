import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ChurnAI - Customer Churn Prediction",
    page_icon="🛒",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

try:
    model = joblib.load("final_churn_model.pkl")
    model_columns = joblib.load("model_columns.pkl")

except Exception as e:

    st.error("❌ Model files could not be loaded.")

    st.write("Make sure these files are in the same folder as app.py:")

    st.code(
        "final_churn_model.pkl\n"
        "model_columns.pkl"
    )

    st.stop()


# ============================================================
# HERO / TITLE
# ============================================================

st.title("🛒 ChurnAI")

st.subheader("AI Customer Intelligence Platform")

st.write(
    "Predict customer churn using machine learning "
    "and transform customer behaviour into actionable "
    "business insights."
)

st.divider()


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.subheader("📌 Project Overview")

info1, info2, info3, info4 = st.columns(4)

with info1:
    st.metric(
        "🤖 AI Model",
        "XGBoost"
    )

with info2:
    st.metric(
        "🎯 Prediction",
        "Real-Time"
    )

with info3:
    st.metric(
        "👥 Customers",
        "50,000+"
    )

with info4:
    st.metric(
        "📊 Target",
        "Churned"
    )


st.divider()


# ============================================================
# CUSTOMER PROFILE
# ============================================================

st.header("👤 Customer Profile")

st.caption(
    "Enter the basic customer information."
)


col1, col2 = st.columns(2)


with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=35,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )

    country = st.selectbox(
        "Country",
        [
            "India",
            "Japan",
            "UK",
            "USA"
        ]
    )

    city = st.selectbox(
        "City",
        [
            "Bangalore",
            "Berlin",
            "Birmingham",
            "Brisbane",
            "Calgary",
            "Chennai",
            "Chicago",
            "Cologne",
            "Delhi",
            "Frankfurt",
            "Glasgow",
            "Hamburg",
            "Houston",
            "Hyderabad",
            "Kyoto",
            "Leeds",
            "London",
            "Los Angeles",
            "Lyon",
            "Manchester",
            "Marseille",
            "Melbourne",
            "Montreal",
            "Mumbai",
            "Munich",
            "Nagoya",
            "New York",
            "Nice",
            "Osaka",
            "Ottawa",
            "Paris",
            "Perth",
            "Phoenix",
            "Sydney",
            "Tokyo",
            "Toronto",
            "Toulouse",
            "Vancouver",
            "Yokohama"
        ]
    )


with col2:

    signup_quarter = st.selectbox(
        "Signup Quarter",
        [
            "Q1",
            "Q2",
            "Q3",
            "Q4"
        ]
    )

    membership_years = st.number_input(
        "Membership Years",
        min_value=0.0,
        value=3.0,
        step=0.5
    )

    login_frequency = st.number_input(
        "Login Frequency",
        min_value=0.0,
        value=15.0,
        step=1.0
    )


st.divider()


# ============================================================
# CUSTOMER BEHAVIOUR
# ============================================================

st.header("📊 Customer Behaviour")

st.caption(
    "Enter customer purchasing and browsing behaviour."
)


col1, col2 = st.columns(2)


with col1:

    session_duration_avg = st.number_input(
        "Session Duration Average",
        min_value=0.0,
        value=30.0,
        step=1.0
    )

    pages_per_session = st.number_input(
        "Pages Per Session",
        min_value=0.0,
        value=8.0,
        step=1.0
    )

    cart_abandonment_rate = st.number_input(
        "Cart Abandonment Rate",
        min_value=0.0,
        value=30.0,
        step=1.0
    )

    wishlist_items = st.number_input(
        "Wishlist Items",
        min_value=0,
        value=3,
        step=1
    )

    total_purchases = st.number_input(
        "Total Purchases",
        min_value=0,
        value=10,
        step=1
    )


with col2:

    average_order_value = st.number_input(
        "Average Order Value",
        min_value=0.0,
        value=500.0,
        step=50.0
    )

    days_since_last_purchase = st.number_input(
        "Days Since Last Purchase",
        min_value=0,
        value=20,
        step=1
    )

    discount_usage_rate = st.number_input(
        "Discount Usage Rate",
        min_value=0.0,
        value=40.0,
        step=1.0
    )

    returns_rate = st.number_input(
        "Returns Rate",
        min_value=0.0,
        value=5.0,
        step=1.0
    )

    email_open_rate = st.number_input(
        "Email Open Rate",
        min_value=0.0,
        value=60.0,
        step=1.0
    )


st.divider()


# ============================================================
# ENGAGEMENT & FINANCIAL
# ============================================================

st.header("💎 Engagement & Financial Details")

st.caption(
    "Enter customer engagement and financial information."
)


col1, col2 = st.columns(2)


with col1:

    customer_service_calls = st.number_input(
        "Customer Service Calls",
        min_value=0,
        value=2,
        step=1
    )

    product_reviews_written = st.number_input(
        "Product Reviews Written",
        min_value=0,
        value=4,
        step=1
    )

    social_media_engagement_score = st.number_input(
        "Social Media Engagement Score",
        min_value=0.0,
        value=50.0,
        step=1.0
    )

    mobile_app_usage = st.number_input(
        "Mobile App Usage",
        min_value=0.0,
        value=70.0,
        step=1.0
    )


with col2:

    payment_method_diversity = st.number_input(
        "Payment Method Diversity",
        min_value=0,
        value=2,
        step=1
    )

    lifetime_value = st.number_input(
        "Lifetime Value",
        min_value=0.0,
        value=5000.0,
        step=100.0
    )

    credit_balance = st.number_input(
        "Credit Balance",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )


st.divider()


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.header("🚀 Customer Churn Prediction")

predict_button = st.button(
    "🚀 ANALYSE CUSTOMER & PREDICT CHURN",
    type="primary",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    try:

        # ----------------------------------------------------
        # CREATE CUSTOMER DATA
        # ----------------------------------------------------

        new_customer = pd.DataFrame(
            [{
                "Age": age,
                "Gender": gender,
                "Country": country,
                "City": city,
                "Membership_Years": membership_years,
                "Total_Purchases": total_purchases,
                "Average_Order_Value": average_order_value,
                "Days_Since_Last_Purchase": days_since_last_purchase,
                "Cart_Abandonment_Rate": cart_abandonment_rate,
                "Wishlist_Items": wishlist_items,
                "Returns_Rate": returns_rate,
                "Discount_Usage_Rate": discount_usage_rate,
                "Login_Frequency": login_frequency,
                "Session_Duration_Avg": session_duration_avg,
                "Pages_Per_Session": pages_per_session,
                "Mobile_App_Usage": mobile_app_usage,
                "Social_Media_Engagement_Score": social_media_engagement_score,
                "Email_Open_Rate": email_open_rate,
                "Product_Reviews_Written": product_reviews_written,
                "Customer_Service_Calls": customer_service_calls,
                "Payment_Method_Diversity": payment_method_diversity,
                "Lifetime_Value": lifetime_value,
                "Credit_Balance": credit_balance,
                "Signup_Quarter": signup_quarter
            }]
        )


        # ----------------------------------------------------
        # ONE HOT ENCODING
        # ----------------------------------------------------

        categorical_columns = [
            "Gender",
            "Country",
            "City",
            "Signup_Quarter"
        ]


        new_customer_encoded = pd.get_dummies(
            new_customer,
            columns=categorical_columns,
            drop_first=False
        )


        # ----------------------------------------------------
        # ALIGN COLUMNS
        # ----------------------------------------------------

        new_customer_encoded = new_customer_encoded.reindex(
            columns=model_columns,
            fill_value=0
        )


        # ----------------------------------------------------
        # PREDICTION
        # ----------------------------------------------------

        prediction = int(
            model.predict(
                new_customer_encoded
            )[0]
        )


        # ----------------------------------------------------
        # PROBABILITY
        # ----------------------------------------------------

        if hasattr(model, "predict_proba"):

            probability = float(
                model.predict_proba(
                    new_customer_encoded
                )[0][1]
            )

        else:

            probability = float(prediction)


        probability_percentage = probability * 100


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.divider()

        st.success(
            "✅ Prediction completed successfully!"
        )


        st.subheader(
            "✨ Customer Intelligence Result"
        )


        result1, result2, result3 = st.columns(3)


        with result1:

            st.metric(
                "🎯 Churn Probability",
                f"{probability_percentage:.2f}%"
            )


        with result2:

            if prediction == 1:

                st.metric(
                    "📌 Prediction",
                    "Likely to Churn"
                )

            else:

                st.metric(
                    "📌 Prediction",
                    "Likely to Stay"
                )


        with result3:

            if probability >= 0.70:

                st.metric(
                    "⚠️ Risk Level",
                    "HIGH"
                )

            elif probability >= 0.40:

                st.metric(
                    "⚠️ Risk Level",
                    "MEDIUM"
                )

            else:

                st.metric(
                    "⚠️ Risk Level",
                    "LOW"
                )


        # ----------------------------------------------------
        # PROBABILITY
        # ----------------------------------------------------

        st.subheader(
            "📈 Churn Probability"
        )

        st.progress(
            min(max(probability, 0.0), 1.0)
        )

        st.write(
            f"Customer churn probability: "
            f"**{probability_percentage:.2f}%**"
        )


        # ----------------------------------------------------
        # RISK MESSAGE
        # ----------------------------------------------------

        if probability >= 0.70:

            st.error(
                "🔴 HIGH RISK CUSTOMER\n\n"
                "This customer has a high probability of churn."
            )

        elif probability >= 0.40:

            st.warning(
                "🟠 MEDIUM RISK CUSTOMER\n\n"
                "This customer may require additional engagement."
            )

        else:

            st.success(
                "🟢 LOW RISK CUSTOMER\n\n"
                "This customer currently shows a lower churn probability."
            )


        # ----------------------------------------------------
        # BUSINESS ACTION
        # ----------------------------------------------------

        st.subheader(
            "💡 Recommended Business Action"
        )


        if probability >= 0.70:

            st.info(
                "🎁 Retention Action:\n\n"
                "• Personalised offers\n"
                "• Targeted discounts\n"
                "• Customer support follow-up\n"
                "• Re-engagement campaigns"
            )

        elif probability >= 0.40:

            st.info(
                "📩 Engagement Action:\n\n"
                "• Personalised recommendations\n"
                "• Email campaigns\n"
                "• Promotional offers"
            )

        else:

            st.info(
                "💚 Customer Action:\n\n"
                "• Continue regular engagement\n"
                "• Maintain personalised experiences\n"
                "• Monitor future behaviour"
            )


        # ----------------------------------------------------
        # CUSTOMER SUMMARY
        # ----------------------------------------------------

        st.subheader(
            "📋 Customer Analysis Summary"
        )


        s1, s2, s3, s4 = st.columns(4)


        with s1:

            st.metric(
                "Age",
                age
            )


        with s2:

            st.metric(
                "Membership",
                f"{membership_years:.1f} years"
            )


        with s3:

            st.metric(
                "Total Purchases",
                total_purchases
            )


        with s4:

            st.metric(
                "Days Since Purchase",
                days_since_last_purchase
            )


        s5, s6, s7, s8 = st.columns(4)


        with s5:

            st.metric(
                "Login Frequency",
                login_frequency
            )


        with s6:

            st.metric(
                "Cart Abandonment",
                f"{cart_abandonment_rate:.0f}%"
            )


        with s7:

            st.metric(
                "Email Open Rate",
                f"{email_open_rate:.0f}%"
            )


        with s8:

            st.metric(
                "Service Calls",
                customer_service_calls
            )


    except Exception as e:

        st.error(
            "❌ Prediction Error"
        )

        st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🛒 ChurnAI • Customer Churn Prediction • "
    "Python • Pandas • XGBoost • Streamlit"
)