import private as private

private UInt16 crc_update (byte data)
{
    int i;
    m_crc = (UInt16)(m_crc ^ ((UInt16)data << 8));
    for (i=0; i<8; i++)
    {
        if ((m_crc & 0x8000)!=0)
             m_crc=(UInt16)((m_crc << 1) ^ 0x1021 );
        else
             m_crc <<= 1;
    }
    return m_crc;
}