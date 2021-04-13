public class ArithmeticsDivision implements IArithmeticsDiv{

    @Override
    public double Division(double A, double B) throws Exception {
        if(B == 0)
        {
            throw new Exception("Dividing by 0");
        }
        else
        {
            return A/B;
        }
    }
}
