import streamlit as st

def main():
    st.title('Cuestionario del Perfil del Inversor')

    with st.form("investment_profile_form"):
        st.write("## 1. ¿Cuál es tu nivel de conocimiento financiero?")
        knowledge = st.selectbox('', ['Ninguno', 'Básico', 'Intermedio', 'Avanzado'], key='1')

        st.write("## 2. ¿Cuál es tu experiencia con inversiones?")
        experience = st.multiselect('', ['Ninguna', 'Depósitos a plazo', 'Fondos comunes de inversión', 'Acciones', 'Bonos', 'Criptomonedas', 'Real Estate'], key='2')

        st.write("## 3. ¿Cuánto tiempo estás dispuesto a dejar tu inversión sin tocarla?")
        investment_period = st.selectbox('', ['Menos de 1 año', '1-3 años', '3-5 años', '5-10 años', 'Más de 10 años'], key='3')

        st.write("## 4. ¿Cuál es tu objetivo principal con la inversión?")
        investment_goal = st.selectbox('', ['Preservación de capital', 'Crecimiento del capital', 'Ingresos regulares', 'Alto rendimiento a largo plazo', 'Alto rendimiento a corto plazo'], key='4')

        st.write("## 5. ¿Cómo reaccionarías si tus inversiones bajan un 10%?")
        loss_reaction = st.selectbox('', ['Vendería todo', 'Vendería parte', 'Mantendría y observaría', 'Invertiría más'], key='5')

        st.write("## 6. ¿Qué porcentaje de tu ingreso estás dispuesto a invertir?")
        income_percentage = st.slider('Seleccione el porcentaje', 0, 100, step=5, key='6')

        st.write("## 7. ¿Qué proporción de tus ahorros invertirías en un producto de alto riesgo y alta recompensa?")
        savings_investment = st.slider('Seleccione el porcentaje', 0, 100, step=5, key='7')

        st.write("## 8. ¿Qué parte de tus inversiones estás dispuesto a perder antes de sentirte incómodo?")
        loss_tolerance = st.slider('Seleccione el porcentaje', 0, 100, step=5, key='8')

        st.write("## 9. ¿Qué nivel de riesgo estás dispuesto a asumir en tus inversiones?")
        risk_level = st.selectbox('', ['Muy bajo', 'Bajo', 'Moderado', 'Alto', 'Muy alto'], key='9')

        st.write("## 10. ¿Con qué frecuencia planeas revisar y ajustar tus inversiones?")
        investment_review = st.selectbox('', ['Semanalmente', 'Mensualmente', 'Cada 3-6 meses', 'Anualmente o menos frecuentemente'], key='10')

        submit_button = st.form_submit_button("Enviar")

        if not all([knowledge, experience, investment_period, investment_goal, loss_reaction, income_percentage,
                    savings_investment, loss_tolerance, risk_level, investment_review]):
            st.write("Por favor, contesta todas las preguntas.")
        else:
            points = calculate_points(knowledge, experience, investment_period, investment_goal, loss_reaction,
                                      income_percentage, savings_investment, loss_tolerance, risk_level,
                                      investment_review)
            investor_profile, profile_description = assign_profile(points)
            st.title(f"Tu perfil de inversor es: {investor_profile}")
            st.write(profile_description)


def calculate_points(knowledge, experience, investment_period, investment_goal, loss_reaction, income_percentage, savings_investment, loss_tolerance, risk_level, investment_review):
    points = 0

    knowledge_dict = {'Ninguno': 0, 'Básico': 2, 'Intermedio': 5, 'Avanzado': 10}
    experience_dict = {'Ninguna': 0, 'Depósitos a plazo': 2, 'Fondos comunes de inversión': 4, 'Acciones': 6, 'Bonos': 8, 'Criptomonedas': 10, 'Real Estate': 5}
    period_dict = {'Menos de 1 año': 10, '1-3 años': 8, '3-5 años': 6, '5-10 años': 4, 'Más de 10 años': 2}
    goal_dict = {'Preservación de capital': 2, 'Crecimiento del capital': 4, 'Ingresos regulares': 6, 'Alto rendimiento a largo plazo': 8, 'Alto rendimiento a corto plazo': 10}
    loss_dict = {'Vendería todo': 0, 'Vendería parte': 4, 'Mantendría y observaría': 7, 'Invertiría más': 10}
    risk_dict = {'Muy bajo': 0, 'Bajo': 2, 'Moderado': 5, 'Alto': 7, 'Muy alto': 10}
    review_dict = {'Semanalmente': 10, 'Mensualmente': 8, 'Cada 3-6 meses': 4, 'Anualmente o menos frecuentemente': 2}

    points += knowledge_dict[knowledge]
    if experience:
        points += max(experience_dict[exp] for exp in experience)
    else:
        points += 0
    points += period_dict[investment_period]
    points += goal_dict[investment_goal]
    points += loss_dict[loss_reaction]
    points += income_percentage // 10
    points += savings_investment // 10
    points += loss_tolerance // 10
    points += risk_dict[risk_level]
    points += review_dict[investment_review]

    return points

def assign_profile(points):

    if points <= 20:
        return 'Muy Conservador', 'Sos un inversor conservador, preferís inversiones de bajo riesgo con baja rentabilidad y tu objetivo es preservar el valor de tu inversión. Estás dispuesto a aceptar menor rendimiento por mayor seguridad, como comprar dólares MEP o FCI a corto plazo.'
    elif points <= 40:
        return 'Conservador', 'Sos un inversor poco arriesgado pero considerarías inversiones con poco riesgo, como podrían ser bonos de gran liquidez de empresas de primer nivel. Tu objetivo principal es preservar el capital en términos reales y aceptar un rendimiento potencial ligeramente menor a cambio de menor riesgo.'
    elif points <= 60:
        return 'Moderado', 'Buscás equilibrio entre riesgo y rendimiento. Podés invertir en una mezcla de bajo y alto riesgo, como por ejemplo realizar inversiones en FCI, bonos de empresas o de países con cotización pública y gran liquidez e incluso acciones de empresas de primer nivel, que muestren volatilidad media o baja. Estás dispuesto a asumir un riesgo moderado a cambio de un rendimiento moderado.'
    elif points <= 80:
        return 'Arriesgado', 'Buscás mayores rendimientos potenciales aceptando un mayor nivel de riesgo. Podés invertir en activos de alto riesgo y alto rendimiento, como por ejemplo acciones o bonos de países emergentes (tanto de países como de empresas operando en esos países), y también invertir en acciones de empresas con alta volatilidad, o empresas relativamente nuevas con corto historial de operaciones. Estás dispuesto a asumir riesgos altos a cambio de mayores ganancias potenciales.'
    else:
        return 'Muy Arriesgado', 'Buscás mayores rendimientos asumiendo alto riesgo. Podés invertir en empresas disruptivas, o activos de renta fija de alto riesgo, como deuda pública de países emergentes con alto riesgo país, o deuda de empresas con riesgos de liquidez o de solvencia.'

if __name__ == "__main__":
    main()